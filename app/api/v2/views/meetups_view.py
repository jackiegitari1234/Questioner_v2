#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.meetup_model import Meetup,check_admin
from app.api.v2.models.auth_model import User
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


@v2.route('/meetups', methods=['POST'])
@jwt_required
def add_meetup():

    current_user = get_jwt_identity()
    print (check_admin(current_user))
    member = check_admin(current_user)
    if member:
        print("is admin")
        user_data = request.get_json()

        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        # Check for empty inputs
        if not all(field in user_data for field in ["topic", "location", "happeningOn","tags"]):
            abort(make_response(jsonify({"message":"Please fill in all the required input fields"}),400))

        topic = user_data['topic']
        location = user_data['location']
        happeningOn = user_data['happeningOn']
        tags = user_data['tags']


        new_meetup = Meetup(topic,location,happeningOn,tags).register_meetup()
        abort(make_response(jsonify({"data":new_meetup}),201))
    abort(make_response(jsonify({"message":"You are not authorised to add a meetup"}),403))




