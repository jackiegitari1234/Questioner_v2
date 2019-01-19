# global builtin modules
import datetime
import os

#downloaded modules
from flask import jsonify,request,abort,make_response,json

#local imports
from app.api.v2 import vers2 as v2


SECRET_KEY = os.getenv("SECRET")


#sign up endpoint
@v2.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    
    
    