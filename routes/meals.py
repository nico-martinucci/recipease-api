from flask import Blueprint, jsonify, request
import queries.meals as q


meals = Blueprint("meals", __name__)


@meals.get("/")
def get_meals():
    """Gets list of all meal types."""

    all_meals = q.get_all_meals()

    return jsonify(all_meals)
