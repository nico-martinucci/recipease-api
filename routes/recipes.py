from flask import Blueprint

recipes = Blueprint("recipes", __name__)

# @app.route('/messages/new', methods=["GET", "POST"])


@recipes.route("/")
def get_recipes():
    return {"message": "recipes!"}
