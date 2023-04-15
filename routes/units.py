from flask import Blueprint, jsonify, request
import queries.units as q


units = Blueprint("units", __name__)


@units.get("/")
def get_units():
    """Returns a list of all units."""

    all_units = q.get_all_units()

    return jsonify(all_units)
