# global builtin modules
import unittest

# local imports
from app import create_app
import Instance

app = create_app("testing")

class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()

        app.config.from_object(Instance.config.TestingConfig)
        self.client = app.test_client()
        

        #authentication
        self.user_1 = {
            "firstname":"jackie",
            "lastname":"gitari"
        }
        self.user_2 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackie@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "kajd23",
            "cpassword" : "kajd23"
            
        }
        self.user_3 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jackiegmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R@kajd23",
            "cpassword" : "R@kajd23"
        }
        self.user_4 = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "jacklinem@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23"
        }
        self.new_user = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "gitari@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23"
        }
        self.nw_user = {
            "firstname" : "jackie",
            "lastname" : "muthoni",
            "othername" : "gitari",
            "email" : "gitari@gmail.com",
            "phoneNumber" : "+254707802693",
            "username" : "jackie",
            "password" : "R#kajd23",
            "cpassword" : "R#kajd23",
            "owner" : "unknown"
        }
  

        return self.client
