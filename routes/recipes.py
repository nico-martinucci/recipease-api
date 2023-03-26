from flask import Blueprint, jsonify, request
import queries.recipes as q

recipes = Blueprint("recipes", __name__)


@recipes.get("/")
def get_recipes():
    """"""


@recipes.post("/")
def add_recipe():
    """Adds a new recipe; Returns new recipe."""

    new_recipe = q.add_new_recipe(
        name=request.json["name"],
        description=request.json["description"],
        username=request.json["username"],
        meal_name=request.json["mealName"],
        type_name=request.json["typeName"],
        private=request.json["private"],
        items=request.json["items"],
        steps=request.json["steps"]
    )

    return jsonify(new_recipe)
