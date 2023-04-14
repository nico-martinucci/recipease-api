from models import RecipeType, db


def get_all_types():
    """
    Gets and returns all type options (e.g. main, side)
    """

    all_types = RecipeType.query.all()

    serialized = [
        {
            "name": type.name,
            "description": type.description
        }
        for type in all_types
    ]

    return {"types": serialized}
