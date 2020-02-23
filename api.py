"""
Your services
"""
from flask import Flask, jsonify
from flask_dotenv import DotEnv
from apis.public import public_api
from apis.private import private_api
from apis.admin import admin_api
from options import PATH_PREFIX
from error import AxiomsError
from flask_cors import CORS

# Flask app
app = Flask(__name__) # pylint: disable=invalid-name
app.config.from_object('config')
env = DotEnv(app)

# Setup CORS globally
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API blueprints, imported after OS.environ
app.register_blueprint(public_api)
app.register_blueprint(private_api)
app.register_blueprint(admin_api)

@app.errorhandler(AxiomsError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# Controllers API
@app.route(PATH_PREFIX, methods=["GET"])
def index():
    """
    Index for this app
    """
    print(app.config)
    return jsonify({'api': 'Your Services'})
