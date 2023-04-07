from flask import Blueprint, jsonify, request
from helpers.auth import authorize
import queries.ratings as q

ratings = Blueprint("ratings", __name__)



