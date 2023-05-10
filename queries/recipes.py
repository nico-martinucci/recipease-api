from models import Recipe, RecipeItem, RecipeStep, RecipeNote, UserRecipe, RecipePhoto, db
from statistics import mean


def get_all_recipes(filter):
    """
    Gets and returns all recipes, optionally filtered by the provided 
    information.
    """

    name_filter = "%{}%".format(filter)
    recipes = Recipe.query.filter(Recipe.name.ilike(name_filter)).all()

    serialized = [
        {
            "id": recipe.id,
            "name": recipe.name,
            "description": recipe.description,
            "photoUrl": recipe.photo_url,
            "mealName": recipe.meal_name,
            "typeName": recipe.type_name,
            "createdBy": recipe.created_by.username,
            "rating": recipe.rating
        }
        for recipe in recipes
    ]

    return {"recipes": serialized}


def get_recipe(recipe_id):
    """Gets and returns a singular recipe, based on the provided id."""

    recipe = Recipe.query.get(recipe_id)

    recipe_items = [
        {
            "id": item.id,
            "amount": item.amount,
            "unit": item.short_unit,
            "ingredient": item.ingredient,
            "description": item.description,
            "order": item.order,
            "subsection": item.subsection
        }
        for item in recipe.items
    ]

    recipe_steps = [
        {
            "id": step.id,
            "description": step.description,
            "order": step.order
        }
        for step in recipe.steps
    ]

    recipe_notes = [
        {
            "id": note.id,
            "timeStamp": note.time_stamp,
            "note": note.note
        }
        for note in recipe.notes
    ]

    serialized = {
        "id": recipe.id,
        "name": recipe.name,
        "description": recipe.description,
        "createdBy": recipe.user_username,
        "mealName": recipe.meal_name,
        "typeName": recipe.type_name,
        "private": recipe.private,
        "photoUrl": recipe.photo_url,
        "items": recipe_items,
        "steps": recipe_steps,
        "notes": recipe_notes
    }

    return {"recipe": serialized}


def add_new_recipe(name, description, createdBy, meal_name, type_name, private,
                   forked_from, items, steps):
    """
    Adds a new recipe to the database with the provided information; Returns
    data about the new recipe.
    """

    new_recipe = Recipe(
        name=name,
        description=description,
        user_username=createdBy,
        meal_name=meal_name,
        type_name=type_name,
        private=private,
        forked_from=forked_from
    )

    db.session.add(new_recipe)
    db.session.commit()

    recipe_items = add_recipe_items(recipe_id=new_recipe.id, items=items)
    recipe_steps = add_recipe_steps(recipe_id=new_recipe.id, steps=steps)

    db.session.commit()

    serialized = {
        "id": new_recipe.id,
        "name": new_recipe.name,
        "description": new_recipe.description,
        "createdBy": new_recipe.user_username,
        "mealName": new_recipe.meal_name,
        "typeName": new_recipe.type_name,
        "private": new_recipe.private,
        "forkedFrom": new_recipe.forked_from,
        "items": recipe_items,
        "steps": recipe_steps
    }

    return {"recipe": serialized}


def add_recipe_items(recipe_id, items):
    """
    Adds new recipe items associated with the provided recipe; Returns a list 
    of added items.
    """

    recipe_items = []

    for item in items:
        new_item = RecipeItem(
            recipe_id=recipe_id,
            order=item["order"],
            amount=item["amount"],
            short_unit=item.get("unit", None),
            ingredient=item["ingredient"],
            description=item.get("description", None),
            subsection=item.get("subsection", None)
        )

        db.session.add(new_item)
        recipe_items.append(new_item)

    # db.session.commit()

    serialized = [
        {
            "id": item.id,
            "order": item.order,
            "amount": item.amount,
            "unit": item.short_unit,
            "ingredient": item.ingredient,
            "description": item.description,
            "subsection": item.subsection
        }
        for item in recipe_items
    ]

    return serialized


def add_recipe_steps(recipe_id, steps):
    """
    Adds new recipe steps associated with the provided recipe; Returns a list 
    of added steps.
    """

    recipe_steps = []

    for step in steps:
        new_step = RecipeStep(
            recipe_id=recipe_id,
            order=step["order"],
            description=step["description"]
        )

        db.session.add(new_step)
        recipe_steps.append(new_step)

    # db.session.commit()

    serialized = [
        {
            "id": step.id,
            "order": step.order,
            "description": step.description
        }
        for step in recipe_steps
    ]

    return serialized


def check_user_recipe_activity(recipe_id, username):
    """
    Checks to see if the provided user has already interacted with the provided
    recipe. If they have, returns a reference to that interaction for 
    modification; if not, creates a new DB entry and returns that reference.
    Used for adding/deleting/modifying notes, starred status, made status, and 
    rating.
    """

    user_recipe_activity = UserRecipe.query.filter(
        UserRecipe.recipe_id == recipe_id,
        UserRecipe.user_username == username
    ).one_or_none()

    if not user_recipe_activity:
        new_activity = UserRecipe(
            user_username=username,
            recipe_id=recipe_id,
        )

        db.session.add(new_activity)
        db.session.commit()

        return new_activity

    return user_recipe_activity


def add_rating_to_recipe(recipe_id, username, rating):
    """
    Adds a rating record to the provided recipe; recalculates average rating and 
    updates the recipe's overall rating; returns the new overall rating.
    """

    user_recipe_activity = check_user_recipe_activity(
        recipe_id=recipe_id,
        username=username
    )

    user_recipe_activity.rating = rating
    db.session.commit()

    # calculate the new average rating for this recipe
    all_recipe_activity = UserRecipe.query.filter(
        UserRecipe.recipe_id == recipe_id
    ).all()

    mean_recipe_rating = mean([
        recipe.rating
        for recipe in all_recipe_activity
    ])

    rated_recipe = Recipe.query.get(recipe_id)
    rated_recipe.rating = mean_recipe_rating

    db.session.commit()

    serialized = {
        "recipeId": rated_recipe.id,
        "rating": rated_recipe.rating,
    }

    return {"rating": serialized}


def add_note_to_recipe(recipe_id, username, note):
    """
    Adds a note to the provided recipe, assuming that the provided username
    matches that of the recipe's creator (notes are reserved for the owner
    of the recipe; comments are public postings for all to see).
    """

    recipe = Recipe.query.get(recipe_id)

    if recipe.created_by.username != username:
        return {"error": "Username doesn't match that of recipe's owner."}

    new_note = RecipeNote(
        recipe_id=recipe_id,
        note=note
    )

    db.session.add(new_note)
    db.session.commit()

    serialized = {
        "id": new_note.id,
        "note": new_note.note
    }

    return serialized


def replace_all_recipe_basics(recipe_id, description, meal_name, type_name, private):
    """
    Replaces all basic recipe information for a given recipe with the provided
    data. Does not change the recipe's name, which can't be changed. Returns
    the updated data.
    """

    recipe = Recipe.query.get(recipe_id)

    recipe.description = description
    recipe.meal_name = meal_name
    recipe.type_name = type_name
    recipe.private = private

    db.session.commit()

    serialized = {
        "description": recipe.description,
        "meal_name": recipe.meal_name,
        "type_name": recipe.type_name,
        "private": recipe.private,
    }

    return {"newBasics": serialized}


def replace_all_recipe_items(recipe_id, items):
    """
    Replaces all current items for a recipe with the items in the provided data
    argument; deletes all current records and writes new ones.
    """

    RecipeItem.query.filter(RecipeItem.recipe_id == recipe_id).delete()

    new_items = add_recipe_items(
        recipe_id=recipe_id,
        items=items
    )

    db.session.commit()

    serialized = {
        "recipeId": recipe_id,
        "items": new_items
    }

    return {"newItems": serialized}


def replace_all_recipe_steps(recipe_id, steps):
    """
    Replaces all current steps for a recipe with the steps in the provided data
    argument; deletes all current records and writes new ones.
    """

    RecipeStep.query.filter(RecipeStep.recipe_id == recipe_id).delete()

    new_steps = add_recipe_steps(
        recipe_id=recipe_id,
        steps=steps
    )

    db.session.commit()

    serialized = {
        "recipeId": recipe_id,
        "steps": new_steps
    }

    return {"newSteps": serialized}


def replace_all_recipe_notes(recipe_id, notes, username):
    """
    Replaces all current steps for a recipes with the notes in the provided data
    argument; deletes all current records and writes new ones.
    """

    RecipeNote.query.filter(RecipeNote.recipe_id == recipe_id).delete()

    new_notes = []

    for note in notes:
        new_notes.append(add_note_to_recipe(
            recipe_id=recipe_id,
            username=username,
            note=note["note"]
        ))

    return {"newNotes": new_notes}


def upload_new_recipe_photo(recipe_id, username, photo_url, caption):
    """
    Adds a new entry to the RecipePhoto table with for the given recipe. If
    the recipe doesn't have a default photo, will add the uploaded photo as
    the default photo. Returns a data object with the url and username. 
    """

    new_photo = RecipePhoto(
        recipe_id=recipe_id,
        uploaded_by=username,
        photo_url=photo_url,
        caption=caption
    )

    db.session.add(new_photo)
    db.session.commit()

    recipe = Recipe.query.get(recipe_id)

    if not recipe.photo_url:
        recipe.photo_url = new_photo.photo_url
        db.session.commit()

    serialized = {
        "username": new_photo.uploaded_by,
        "photoUrl": new_photo.photo_url,
        "caption": new_photo.caption
    }

    return {"newPhoto": serialized}


def update_recipe_cover_photo(recipe_id, photo_url):
    """
    Updates the given recipe's cover photo with the provided photoUrl. Doesn't
    return anything.
    """

    recipe = Recipe.query.get(recipe_id)

    recipe.photo_url = photo_url

    db.session.commit()
