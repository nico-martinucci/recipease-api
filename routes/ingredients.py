from flask import Blueprint, jsonify, request
from helpers.auth import authorize
import queries.ingredients as q


ingredients = Blueprint("ingredients", __name__)


@ingredients.get("/")
def get_ingredients():
    """
    Gets a list of ingredients, optionally filtered by the value in the query 
    string.
    """

    ingredients = q.get_ingredients(request.args.get("nameLike", ""))

    return jsonify(ingredients)


@ingredients.post("/")
@authorize
def add_ingredient():
    """Adds a new ingredient."""

    new_ingredient = q.add_new_ingredient(
        name=request.json["name"],
        description=request.json["description"],
        category=request.json["category"]
    )

    return jsonify(new_ingredient)
