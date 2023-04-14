from flask import Blueprint, jsonify, request
import queries.types as q


types = Blueprint("types", __name__)


@types.get("/")
def get_types():
    """Gets list of all recipe types."""

    all_types = q.get_all_types()

    return jsonify(all_types)
