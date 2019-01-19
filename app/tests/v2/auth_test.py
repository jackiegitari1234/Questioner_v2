# global builtin modules
import unittest
import json

# local imports
from app import create_app
from .base_test import BaseTest
import Instance

app = create_app("testing")


class TestAuth(BaseTest):

    '''SIGN UP'''
    # test json_data
    def test_post_meetup(self):
        response = self.client.post('api/v1/signup')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Application/JSON post expected")
        self.assertEqual(response.status_code, 400)

    # Test empty fields
    def test_empty_signup_fields(self):
        response = self.client.post('api/v1/signup', data=json.dumps(self.user_1), 
                                    content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "All fields are required")
        self.assertEqual(response.status_code, 400)

    # Test register with invalid password
    def test_signup_invalid_password(self):
        response = self.client.post('api/v1/signup', data=json.dumps(self.user_2), 
                                    content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Your password is not valid")
        self.assertEqual(response.status_code, 400)

    # Test register with invalid email
    def test_signup_invalid_email(self):
        response = self.client.post('api/v1/signup', data=json.dumps(self.user_3), 
                                    content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Your email is not valid")
        self.assertEqual(response.status_code, 400)

    # Test valid registration
    def test_signup_valid_input(self):
        response = self.client.post('api/v1/signup', data=json.dumps(self.new_user), 
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)  # 201 created

    # Test registration with more than the required fields
    def test_register_with_more_than_the_required_fields(self):
        response = self.client.post('api/v1/signup',data=json.dumps(self.nw_user), 
                                    content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "All fieds are required ")
