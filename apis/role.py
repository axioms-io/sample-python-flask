"""
Private API with role based access
"""
from flask import Blueprint
from flask import jsonify, request
from axioms_flask.decorators import has_valid_access_token, has_required_roles

role_api = Blueprint("role_api", __name__)  # pylint: disable=invalid-name


@role_api.route("/role", methods=["GET", "POST", "PATCH", "DELETE"])
@has_valid_access_token
@has_required_roles(["sample:role"])
def sample_role():
    """
    Sample role - create, update, read, delete
    """
    if request.method == 'POST':
        return jsonify({"message": "Sample created."})
    if request.method == 'PATCH':
        return jsonify({"message": "Sample updated."})
    if request.method == 'GET':
        return jsonify({"message": "Sample read."})
    if request.method == 'DELETE':
        return jsonify({"message": "Sample deleted."})
