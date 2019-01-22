#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v2 import vers2 as v2


@v2.route('/meetups', methods=['POST'])
def add_meetup():

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


    Meetup = meetup(topic,location,happeningOn,tags).add_Meetup()
    abort(make_response(jsonify({"data":Meetup}),201))




