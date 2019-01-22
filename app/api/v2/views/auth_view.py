# global builtin modules
import datetime
import os

# downloaded modules
from flask import jsonify, request, abort, make_response, json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.auth_model import User
from app.api.v2.utils.validator import inputs_validate, hash_password
from app.api.v2.utils.database import init_db

inputs_validate = inputs_validate()


SECRET_KEY = os.getenv("SECRET")
# app.config['JWT_SECRET_KEY'] = SECRET_KEY  # Change this!
# jwt = JWTManager(app)


# sign up endpoint
@v2.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    if not data:
        abort(make_response(
            jsonify({"message": "POST of type Application/JSON expected"}),
            400))

    # Check for empty inputs
    if not all(field in data for field in ["firstname", "lastname",
                                           "othername", "email",
                                           "phone_number",
                                           "username", "password",
                                           "cpassword"]):
        abort(make_response(
            jsonify({"message": "All fields are required"}), 400))

    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    username = data['username']
    email = data['email']
    phone_number = data['phone_number']
    password = data['password']
    cpassword = data['cpassword']

    # validate email
    if not inputs_validate.email_validation(email):
        abort(make_response(
            jsonify({"message": "Your email is not valid"}), 400))

    # validate password
    if not inputs_validate.password_validation(password):
        abort(make_response(
            jsonify({"message": "Your password is not valid"}), 400))

    if not inputs_validate.compare_password(password, cpassword):
        abort(make_response(
            jsonify({"message": "Passwords do not match"}), 400))

    pwd = hash_password(password)  # encrypt the password
    new_user = User(firstname, lastname, othername,
                    username, email, phone_number, pwd)
    mb = new_user.register_user()
    if mb is None:
        return make_response(jsonify(
            {"message": "Email had already registered",
             "status": 400}))
    else:
        return make_response(jsonify({"message": "successfully registered",
                                      "status": 201}), 201)

# sign in endpoint


@v2.route('/signin', methods=['POST'])
def login():

    data = request.get_json()
    if not data:
        abort(make_response(
            jsonify({"message": "POST of type Application/JSON expected"}),
            400))

    # Check for empty inputs
    if not all(field in data for field in ["email", "password"]):
        abort(make_response(
            jsonify({"message": "Email and Paswword are required"}), 400))

    email = data['email']
    password = data['password']

    # validate email
    if not inputs_validate.email_validation(email):
        abort(make_response(
            jsonify({"message": "Please enter a valid email"}), 400))

    # check if email exists
    cur = init_db().cursor()
    query = "SELECT email from member WHERE email = %s;"
    cur.execute(query, (data['email'],))
    user_data = cur.fetchone()
    cur.close()

    if not user_data:
        abort(make_response(jsonify({"message": "User not Found"}), 404))


    # check if password exists
    cur = init_db().cursor()
    query = "SELECT password from member WHERE email = %s;"
    cur.execute(query, (data['email'],))
    user_data = cur.fetchone()
    cur.close()

    details = (user_data[0])
    if not inputs_validate.check_password(details, data['password']):
        print (inputs_validate.check_password(user_data, data['password']))
        abort(make_response(
            jsonify({"message": "Wrong Password"}), 400))

    # abort(make_response(jsonify({"message": "user logged in"}), 200))
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200
