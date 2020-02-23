"""
Private APIs
"""
from flask import Blueprint
from flask import jsonify
from options import PATH_PREFIX
from utils.decorators import is_authenticated, has_required_scopes

admin_api = Blueprint('admin_api', __name__) # pylint: disable=invalid-name

@admin_api.route(PATH_PREFIX+'admin', methods=["GET"])
@is_authenticated
@has_required_scopes(['tenant:owner'])
def api_private():
    """
    Private admin endpoint
    """
    return jsonify({'message': 'All good. You are authenticated as admin!'})
