from models import Recipe, RecipeItem, RecipeStep, RecipeNote, UserRecipe, db
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
            "photo_url": recipe.photo_url,
            "meal_name": recipe.meal_name,
            "type_name": recipe.type_name,
            "created_by": recipe.created_by.username,
            "rating": recipe.rating
        }
        for recipe in recipes
    ]

    return {"recipes": serialized}


def get_recipe():
    """Gets and returns a singular recipe, based on the provided id."""


def add_new_recipe(name, description, username, meal_name, type_name, private,
                   items, steps):
    """
    Adds a new recipe to the database with the provided information; Returns
    data about the new recipe.
    """

    new_recipe = Recipe(
        name=name,
        description=description,
        user_username=username,
        meal_name=meal_name,
        type_name=type_name,
        private=private
    )

    db.session.add(new_recipe)
    db.session.commit()

    recipe_items = add_recipe_items(recipe_id=new_recipe.id, items=items)
    recipe_steps = add_recipe_steps(recipe_id=new_recipe.id, steps=steps)

    serialized = {
        "id": new_recipe.id,
        "name": new_recipe.name,
        "description": new_recipe.description,
        "created_by": new_recipe.user_username,
        "meal_name": new_recipe.meal_name,
        "type_name": new_recipe.type_name,
        "private": new_recipe.private,
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
            description=item.get("description", None)
        )

        db.session.add(new_item)
        recipe_items.append(new_item)

    db.session.commit()

    serialized = [
        {
            "id": item.id,
            "order": item.order,
            "amount": item.amount,
            "unit": item.short_unit,
            "ingredient": item.ingredient,
            "description": item.description
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

    db.session.commit()

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
        "recipe_id": rated_recipe.id,
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
        "note": new_note.note
    }

    return serialized