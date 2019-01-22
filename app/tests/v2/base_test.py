# global builtin modules
import unittest
import os

# local imports
from app import create_app
from app.api.v2.utils.database import init_db, create_tables, drop_all_tables
import Instance
from Instance.config import app_config

app = create_app(config="testing")


class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        self.client = create_app(config="testing").test_client()
        config = os.getenv("TESTING_ENV")
        init_db()
        print(config)
        create_tables()

        # authentication
        self.user_1 = {
            "firstname": "jackie",
            "lastname": "gitari"
        }
        self.user_2 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "mary@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "kajd23",
            "cpassword": "kajd23"

        }
        self.user_3 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "lukegmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.user_4 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "jacklinem@gmail.com",
            "phoneNumber": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.new_user = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "mee123l@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.nw_user = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "luke@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }

        return self.client
