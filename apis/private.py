"""
Private API
"""
from flask import Blueprint
from flask import jsonify
from axioms_flask.decorators import has_valid_access_token, has_required_scopes

private_api = Blueprint("private_api", __name__)  # pylint: disable=invalid-name


@private_api.route("/private", methods=["GET"])
@has_valid_access_token
@has_required_scopes(["openid", "profile"])
def api_private():
    """
    Private API - authentication required
    """
    return jsonify({"message": "All good. You are authenticated!"})
