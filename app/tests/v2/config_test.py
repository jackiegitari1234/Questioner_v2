# global builtin modules
import unittest

# local imports
from app import create_app
from .base_test import BaseTest
import Instance

app = create_app("testing")


class TestAuth(BaseTest):
    def test_if_app_is_launching(self):
        res = "Hello World!"
        response = self.client.get('/')
        assert res in response.data
        assert response.status_code == 200
