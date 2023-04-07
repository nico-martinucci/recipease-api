from flask import Blueprint, jsonify, request
from helpers.auth import authorize
import queries.ratings as q

ratings = Blueprint("ratings", __name__)


@ratings.post("/<int:recipe_id>")
@authorize
def add_rating(recipe_id):
    """
    Adds a new rating to the provided recipe; recalculates the average rating 
    and writes to recipe.
    """

    # TODO: update to username from JWT once auth is implemented
    avg_rating = q.add_rating_to_recipe(
        recipe_id=recipe_id,
        username=request.json["username"],
        rating=request.json["rating"]
    )

    return jsonify(avg_rating)
