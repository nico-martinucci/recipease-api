from flask import Blueprint, jsonify, request
from helpers.auth import authorize
import queries.recipes as q
import helpers.s3_upload as f


recipes = Blueprint("recipes", __name__)


@recipes.get("/")
def get_recipes():
    """
    Returns a list of all recipes, optionally filtered by the provided criteria.
    """

    # FIXME: removing the more complicated filtering for now - this is going to
    # take some doing to figure out. for now, going to implement a version that
    # just takes
    # filters = {
    #     "ingredients": request.args.get("ingredients", ""),
    #     "minRating": request.args.get("minRating", 0),
    #     "saved": request.args.get("saved", False),
    #     "meal": request.args.get("meal", ""),
    #     "type": request.args.get("type", ""),
    #     "made": request.args.get("made", False),
    #     "name": request.args.get("name", "")
    # }

    # if filters["ingredients"]:
    #     filters["ingredients"] = filters["ingredients"].split(",")

    # if filters["meal"]:
    #     filters["meal"] = filters["meal"].split(",")

    # if filters["type"]:
    #     filters["type"] = filters["type"].split(",")

    # print(filters)

    # FIXME: figure out how to pass these to the function below. not sure the
    # best way to handle - some filters live on recipe, some live in
    # ingredients, and some are living on the recipe/user relationship.

    recipes = q.get_all_recipes(request.args.get("name", ""))

    return jsonify(recipes)


@recipes.post("/")
@authorize
def add_recipe():
    """Adds a new recipe; Returns new recipe."""

    new_recipe = q.add_new_recipe(
        name=request.json["name"],
        description=request.json["description"],
        createdBy=request.json["createdBy"],
        meal_name=request.json["mealName"],
        type_name=request.json["typeName"],
        private=request.json["private"],
        items=request.json["items"],
        steps=request.json["steps"]
    )

    return jsonify(new_recipe)


@recipes.post("/<int:recipe_id>/photos")
@authorize
def add_photo_to_recipe(recipe_id):
    """Adds a new photo to the given recipe."""

    photo_url = f.post_new_file(request.files["photo"])

    new_photo = q.upload_new_recipe_photo(
        recipe_id=recipe_id,
        username=request.form["username"],
        photo_url=photo_url,
        caption=request.form["caption"]
    )

    if request.form["makeCover"].lower() == "true":
        q.update_recipe_cover_photo(
            recipe_id=recipe_id,
            photo_url=photo_url
        )

    return jsonify(new_photo)


@recipes.get("/<int:recipe_id>")
def get_recipe(recipe_id):
    """Gets a single recipe by id."""

    recipe = q.get_recipe(recipe_id=recipe_id)

    return jsonify(recipe)


@recipes.post("/<int:recipe_id>/ratings")
@authorize
def add_rating(recipe_id):
    """
    Adds a new rating to the provided recipe; recalculates the average rating 
    and writes to recipe.
    """

    avg_rating = q.add_rating_to_recipe(
        recipe_id=recipe_id,
        username=request.json["username"],
        rating=request.json["rating"]
    )

    return jsonify(avg_rating)


@recipes.post("/<int:recipe_id>/notes")
@authorize
def add_note(recipe_id):
    """
    Adds a new note to the provided recipe.
    """

    new_note = q.add_note_to_recipe(
        recipe_id=recipe_id,
        username=request.json["username"],
        note=request.json["note"]
    )

    return jsonify(new_note)


@recipes.put("/<int:recipe_id>/basics")
@authorize
def update_recipe_basics(recipe_id):
    """
    Updates all recipes basics (except the recipe's name).
    """

    new_basics = q.replace_all_recipe_basics(
        recipe_id=recipe_id,
        description=request.json["description"],
        meal_name=request.json["mealName"],
        type_name=request.json["typeName"],
        private=request.json["private"]
    )

    return jsonify(new_basics)


@recipes.put("/<int:recipe_id>/items")
@authorize
def update_recipe_items(recipe_id):
    """
    Updates all items for a given recipe.
    """

    new_items = q.replace_all_recipe_items(
        recipe_id=recipe_id,
        items=request.json["items"]
    )

    return jsonify(new_items)


@recipes.put("/<int:recipe_id>/steps")
@authorize
def update_recipe_steps(recipe_id):
    """
    Updates all steps for a given recipe.
    """

    new_steps = q.replace_all_recipe_steps(
        recipe_id=recipe_id,
        steps=request.json["steps"]
    )

    return jsonify(new_steps)


@recipes.put("/<int:recipe_id>/notes")
@authorize
def update_recipe_notes(recipe_id):
    """
    Update all notes for a given recipe.
    """

    new_notes = q.replace_all_recipe_notes(
        recipe_id=recipe_id,
        notes=request.json["notes"],
        username=request.json["username"]
    )

    return jsonify(new_notes)
