"""
Public APIs
"""
from flask import Blueprint
from flask import jsonify
from options import PATH_PREFIX

public_api = Blueprint('public_api', __name__) # pylint: disable=invalid-name

@public_api.route(PATH_PREFIX+'public', methods=["GET"])
def api_public():
    """
    Public endpoint
    """
    return jsonify({'message': 'Hello from a public endpoint!'})
