from models import Meal, db


def get_all_meals():
    """
    Gets and returns all meal options (e.g. dinner, lunch)
    """

    all_meals = Meal.query.all()

    serialized = [
        {
            "name": meal.name,
            "description": meal.description
        }
        for meal in all_meals
    ]

    return {"meals": serialized}
