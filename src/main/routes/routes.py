from flask import Blueprint, request, jsonify

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"