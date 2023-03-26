from models import Recipe, RecipeItem, RecipeStep, db


def get_all_recipes():
    """
    Gets and returns all recipes, optionally filtered by the provided 
    information.
    """


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
