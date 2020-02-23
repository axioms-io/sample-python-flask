"""
Private APIs
"""
from flask import Blueprint
from flask import jsonify
from options import PATH_PREFIX
from utils.decorators import is_authenticated, has_required_scopes

private_api = Blueprint('private_api', __name__) # pylint: disable=invalid-name

@private_api.route(PATH_PREFIX+'private', methods=["GET"])
@is_authenticated
@has_required_scopes(['openid', 'profile'])
def api_private():
    """
    Private endpoint
    """
    return jsonify({'message': 'All good. You are authenticated!'})
