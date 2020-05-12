"""
Private API with permission based access
"""
from flask import Blueprint
from flask import jsonify
from axioms_flask.decorators import is_authenticated, has_required_permissions

permission_api = Blueprint("permission_api", __name__)  # pylint: disable=invalid-name


@permission_api.route("/permission", methods=["POST"])
@is_authenticated
@has_required_permissions(["sample:create"])
def sample_create():
    """
    Create sample
    """
    return jsonify({"message": "Sample created."})


@permission_api.route("/permission", methods=["PATCH"])
@is_authenticated
@has_required_permissions(["sample:update"])
def sample_update():
    """
    Update sample
    """
    return jsonify({"message": "Sample updated."})


@permission_api.route("/permission", methods=["GET"])
@is_authenticated
@has_required_permissions(["sample:read"])
def sample_read():
    """
    Read sample
    """
    return jsonify({"message": "Sample read."})


@permission_api.route("/permission", methods=["DELETE"])
@is_authenticated
@has_required_permissions(["sample:delete"])
def sample_delete():
    """
    Delete sample
    """
    return jsonify({"message": "Sample deleted."})
