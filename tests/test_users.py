from api.models.user import User
from tests.base_test import BaseTestCase
from flask import json


class TestUsers(BaseTestCase):
    def setUp(self):
        kwargs = {
            "user_id": 1,
            "full_name": "Adralia Nelson",
            "email": "nadralia@gmail.com",
            "gender": "male",
            "username": "nadralia",
            "password": "1234567#ad",
            "role": "admin"
        }
        self.user = User(**kwargs)