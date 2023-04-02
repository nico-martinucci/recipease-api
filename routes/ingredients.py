from flask import Blueprint, jsonify, request
import queries.ingredients as q


ingredients = Blueprint("ingredients", __name__)


@ingredients.get("/")
def get_ingredients():
    """
    Gets a list of ingredients, optionally filtered by the value in the query 
    string.
    """

    # TODO: add authentication

    ingredients = q.get_ingredients(request.args["nameLike"])

    return jsonify(ingredients)


@ingredients.post("/")
def add_ingredient():
    """Adds a new ingredient."""

    # TODO: add authentication

    new_ingredient = q.add_new_ingredient(
        name=request.json["name"],
        description=request.json["description"],
        category=request.json["category"]
    )

    return jsonify(new_ingredient)
