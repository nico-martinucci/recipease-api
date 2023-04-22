from models import IngredientCategory, db


def get_all_categories():
    """
    Gets and returns all ingredient category options.
    """

    all_categories = IngredientCategory.query.all()

    serialized = [
        {
            "name": cat.name,
            "description": cat.description
        }
        for cat in all_categories
    ]

    return {"categories": serialized}
