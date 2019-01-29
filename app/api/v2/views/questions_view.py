#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v2 import vers2 as v2
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

@v2.route('/meetups/<int:id>/rsvp', methods=['POST'])
# @jwt_required
def add_meetup():
    user_data = request.get_json()

        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        # Check for empty inputs
        if not all(field in user_data for field in ["question"]):
            abort(make_response(jsonify({"message":"Please fill in a question"}),400))

        topic = user_data['question']

