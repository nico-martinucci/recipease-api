from models import db, Ingredient


def get_ingredients(name):
    """
    Gets list of ingredients, filtered by the provided name parameter.
    """

    filter = "%{}%".format(name)
    ingredients = Ingredient.query.filter(Ingredient.name.ilike(filter))

    serialized = [
        {
            "name": i.name,
            "description": i.description,
            "category": i.category
        }
        for i in ingredients
    ]

    return {"ingredients": serialized}


def add_new_ingredient(name, description, category):
    """
    Adds a new ingredient to the database with the provided information;
    returns the info about the new ingredient.
    """

    dupe_ingredient = Ingredient.query.get(name)

    if dupe_ingredient:
        return {"error": "This ingredient has already been added."}

    new_ingredient = Ingredient(
        name=name,
        description=description,
        category=category
    )

    db.session.add(new_ingredient)
    db.session.commit()

    serialized = {
        "name": new_ingredient.name,
        "description": new_ingredient.description,
        "category": new_ingredient.category
    }

    return {"ingredient": serialized}
