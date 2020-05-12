"""
Public API
"""
from flask import Blueprint
from flask import jsonify

public_api = Blueprint("public_api", __name__)  # pylint: disable=invalid-name


@public_api.route("/public", methods=["GET"])
def api_public():
    """
    Public API - no authentication required
    """
    return jsonify({"message": "Hello from a public endpoint!"})
