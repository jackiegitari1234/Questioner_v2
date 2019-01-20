# global builtin modules
import datetime
import os

# downloaded modules
from flask import jsonify, request, abort, make_response, json

# local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.auth_model import User


SECRET_KEY = os.getenv("SECRET")


# sign up endpoint
@v2.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()

    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    email = data['email']
    password = data['password']

    new_user = User(firstname, lastname, othername, username, email, password)
    new_user.register_user()
    return data
    
    
    