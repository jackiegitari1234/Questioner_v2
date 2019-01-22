'''ENTRY POINT OF THE APP'''
# global builtin modules
import os
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# local imports
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
SECRET_KEY = os.getenv("SECRET")
app.config['JWT_SECRET_KEY'] = SECRET_KEY  # Change this!
jwt = JWTManager(app)


@app.route('/')
def index():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)
