'''THIS IS THE GLUE'''

# downloaded modules
from flask import Flask, jsonify

# local imports
from Instance.config import app_config
from app.api.v2.views.auth_view import v2 as V2_auth
from app.api.v2.views.meetups_view import v2 as V2_meetups
from app.api.v2.views.questions_view import v2 as V2_questions
from app.api.v2.utils.errorhandlers import (page_not_found,
                                            server_error, invalid_method,
                                            bad_request)
from app.api.v2.utils.database import init_db, create_tables


def create_app():

    app = Flask(__name__)
    app.register_blueprint(V2_auth)
    app.register_blueprint(V2_meetups)
    app.register_blueprint(V2_questions)
    
    init_db()
    create_tables()

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(400, bad_request)

    return app
