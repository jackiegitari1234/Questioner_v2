# global builtin modules
import unittest
import Instance
import json

# local imports
import os
from app import create_app
from .base_test import BaseTest
from app.api.v2.utils.database import init_db, create_tables

# app = create_app("testing")


class TestAuth(BaseTest):

    '''SIGN UP'''

    # test json data
    config = os.getenv("TESTING_ENV")

    init_db()
    create_tables()

    def test_post_meetup(self):
        response = self.client.post('api/v2/signup')
        result = json.loads(response.data)
        self.assertEqual(result["message"],
                         "POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signup_fields(self):
        response = self.client.post(
            'api/v2/signup', data=json.dumps(self.user_1),
            content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "All fields are required")
        self.assertEqual(response.status_code, 400)

    # Test register with invalid password
    def test_signup_invalid_password(self):
        response = self.client.post(
            'api/v2/signup', data=json.dumps(self.user_2),
            content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Your password is not valid")
        self.assertEqual(response.status_code, 400)

    # Test register with invalid email
    def test_signup_invalid_email(self):
        response = self.client.post(
            'api/v2/signup', data=json.dumps(self.user_3),
            content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Your email is not valid")
        self.assertEqual(response.status_code, 400)

    # Test register with invalid email
    def test_signup_valid_details(self):
        config = "testing"
        init_db()
        create_tables()
        response = self.client.post(
            'api/v2/signup', data=json.dumps(self.new_user),
            content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "successfully registered")
        self.assertEqual(response.status_code, 201)
       

