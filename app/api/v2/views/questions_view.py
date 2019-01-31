#downloaded modules
from flask import jsonify,request,abort,make_response
from app.api.v2.models.questions_model import Question
from app.api.v2.models.meetup_model import check_meet

#local imports
from app.api.v2 import vers2 as v2
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

@v2.route('/meetups/<int:id>/questions', methods=['POST'])
@jwt_required
def add_question(id):
    if check_meet(id) == True:
        user_data = request.get_json()

        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        # Check for empty inputs
        if not all(field in user_data for field in ["title", "body"]):
            abort(make_response(jsonify({"message":"Please fill in the title and body fields"}),400))

        title = user_data['title']
        body = user_data['body']
        username = get_jwt_identity()

        new_quiz = Question(id,username,title,body).add_quiz()
        abort(make_response(jsonify({"data":new_quiz}),201))
    abort(make_response(jsonify({"message":"Meetup not found"}),400))

@v2.route('/questions/<int:id>/comment', methods=['POST'])
def add_comment(id):
        user_data = request.get_json()

        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        if not all(field in user_data for field in ["comment"]):
            abort(make_response(jsonify({"message":"Please fill in a comment"}),400))

        comment = user_data['comment']
        username = get_jwt_identity()


