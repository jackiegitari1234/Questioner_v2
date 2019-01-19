'''THIS IS THE GLUE'''

#downloaded modules
from flask import Flask, jsonify

# local imports
from Instance.config import app_config
from app.api.v2.views.auth_view import v2 as V2_auth

#edge
def invalid_method(error):
    return jsonify({
        'error': str(error),
        'status': 405
        }), 405

#bad request
def bad_request(error):
    return jsonify({
        'error': str(error),
        'status': 400
        }), 400

#unexisting url
def page_not_found(error):
    return jsonify({
        'error': str(error),
        'status': 404
        }), 404

#internal server error
def server_error(error):
    return jsonify({
        'error': str(error),
        'status': 500
        }), 500



def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(app_config["development"])
    app.register_blueprint(V2_auth)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(400, bad_request)

    return app

