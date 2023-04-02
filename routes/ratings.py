from flask import Blueprint, jsonify, request
import queries.ratings as q

ratings = Blueprint("ratings", __name__)


@ratings.post("/<int:recipe_id>")
def add_rating(recipe_id):
    """
    Adds a new rating to the provided recipe; recalculates the average rating 
    and writes to recipe.
    """

    # TODO: add authentication

    # TODO: update to username from JWT once auth is implemented
    avg_rating = q.add_rating_to_recipe(
        recipe_id=recipe_id,
        username="test",
        rating=request.json["rating"]
    )

    return jsonify(avg_rating)
