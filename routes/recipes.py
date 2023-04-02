from flask import Blueprint, jsonify, request
import queries.recipes as q


recipes = Blueprint("recipes", __name__)


@recipes.get("/")
def get_recipes():
    """
    Returns a list of all recipes, optionally filtered by the provided criteria.
    """

    filters = {
        "ingredients": request.args.get("ingredients", ""),
        "minRating": request.args.get("minRating", 0),
        "saved": request.args.get("saved", False),
        "meal": request.args.get("meal", ""),
        "type": request.args.get("type", ""),
        "made": request.args.get("made", False),
        "name": request.args.get("name", "")
    }

    if filters["ingredients"]:
        filters["ingredients"] = filters["ingredients"].split(",")

    if filters["meal"]:
        filters["meal"] = filters["meal"].split(",")

    if filters["type"]:
        filters["type"] = filters["type"].split(",")

    print(filters)

    # FIXME: figure out how to pass these to the function below. not sure the
    # best way to handle - some filters live on recipe, some live in
    # ingredients, and some are living on the recipe/user relationship.

    recipes = q.get_all_recipes()

    return jsonify(recipes)


@recipes.post("/")
def add_recipe():
    """Adds a new recipe; Returns new recipe."""

    # TODO: add authentication

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
