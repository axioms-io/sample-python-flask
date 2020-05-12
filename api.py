"""
Flask Sample APIs
"""
from flask import Flask, jsonify
from flask_dotenv import DotEnv
from apis.public import public_api
from apis.private import private_api
from apis.role import role_api
from apis.permission import permission_api
from axioms_flask.error import AxiomsError
from flask_cors import CORS

# Flask app
app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object("config")
env = DotEnv(app)

# Setup CORS globally
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API blueprints, imported after OS.environ
app.register_blueprint(public_api)
app.register_blueprint(private_api)
app.register_blueprint(role_api)
app.register_blueprint(permission_api)


@app.errorhandler(AxiomsError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    response.headers[
        "WWW-Authenticate"
    ] = "Bearer realm='{}', error='{}', error_description='{}'".format(
        app.config["AXIOMS_DOMAIN"], ex.error["error"], ex.error["error_description"]
    )
    return response


# Controllers API
@app.route("/", methods=["GET"])
def index():
    """
    Index for this app
    """
    return jsonify({"api": "Flask Sample APIs"})
