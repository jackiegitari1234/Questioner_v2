# global builtin modules
import datetime
import os

# downloaded modules
from flask import jsonify, request, abort, make_response, json

# local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.auth_model import User
from app.api.v2.utils.validator import inputs_validate,hash_password

inputs_validate = inputs_validate()


SECRET_KEY = os.getenv("SECRET")


# sign up endpoint
@v2.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    if not data:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))

    # Check for empty inputs
    if not all(field in data for field in ["firstname", "lastname", "othername", "email", "phone_number", "username", "password", "cpassword" ]):
        abort(make_response(jsonify({"message":"All fields are required"}),400))

    
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    username = data['username']
    email = data['email']
    phone_number = data['phone_number']
    password = data['password']
    cpassword = data['cpassword']

     #validate email
    if not inputs_validate.email_validation(email):
        abort(make_response(jsonify({"message":"Your email is not valid"}),400))

    #validate password
    if not inputs_validate.password_validation(password):
        abort(make_response(jsonify({"message":"Your password is not valid"}),400))

    if not inputs_validate.compare_password(password, cpassword):
        abort(make_response(jsonify({"message":"Passwords do not match"}),400))

    pwd = hash_password(password) #encrypt the password
    new_user = User(firstname, lastname, othername, username, email,phone_number, pwd)
    mb = new_user.register_user()
    if mb == None:
        return make_response(jsonify({"message": "user not registered",
                                        "status": 400}))
    else:
        return make_response(jsonify({"message": "user successfully registered",
                                        "status": 201})), 201

    
    
    