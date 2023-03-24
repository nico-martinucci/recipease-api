from flask import Blueprint, jsonify
from models import db, Meal

recipes = Blueprint("recipes", __name__)

# @app.route('/messages/new', methods=["GET", "POST"])


@recipes.route("/")
def get_recipes():

    meals = Meal.query.all()
    serial_meals = [meal.serialize() for meal in meals]

    return jsonify({"meals": serial_meals})
