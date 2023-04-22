from flask import Blueprint, jsonify, request
import queries.categories as q


categories = Blueprint("categories", __name__)


@categories.get("/")
def get_categories():
    """Gets list of all categories."""

    all_categories = q.get_all_categories()

    return jsonify(all_categories)
