import unittest
from api.validations import Validation
from api import app


class TestValidation(unittest.TestCase):
    """ Tests Reflag and user validations """

    def setUp(self):
        """Sets up the validation class """
        self.validation = Validation()

    def test_validate_reflag(self):
        # Tests to ensure the correct data definition passes
        data = {
            "comment": "Police extortion",
            "createdBy": "Adralia Nelson",
            "email": "nadralia@gmail.com",
            "images": "rigg.jpg",
            "location": "kansanga",
            "status": "draft",
            "type": "red-flag",
            "videos": "rig.mp4"
        }
        self.assertEqual(self.validation.redflag_validation(data['comment'],data['location'],data['type']), "Valid")
    
    def test_validate_reflag_empty_comment(self):
        # Tests to ensure the correct data definition passes
        data = {
            "comment":"",
            "createdBy": "Adralia Nelson",
            "email": "nadralia@gmail.com",
            "images": "rigg.jpg",
            "location": "kansanga",
            "status": "draft",
            "type": "red-flag",
            "videos": "rig.mp4"
        }
        self.assertEqual(self.validation.redflag_validation(data['comment'],data['location'],data['type']), 
        "Comment of the redflag is missing")

    def test_validate_user(self):
        # Tests to ensure the correct user data definition passes
        data = {
            "firstname": "Adralia",
            "lastname": "Nelson",
            "email": "nadralia@gmail.com",
            "gender": "Male",
            "username": "nadralia",
            "password": "nadra2526#A",
            "role": "Reporter"
        }
        self.assertEqual(self.validation.validate_user(data['username'],data['email'],data['gender']), "is_valid")

    def test_validate_user_login(self):
        # Tests to ensure the correct user data definition passes
        data = {
            "username": "nadralia",
            "password": "nadra2526#A"
        }
        self.assertEqual(self.validation.validate_login(data['username'],data['password']), "Credentials valid")

    def test_validate_login_empty_username(self):
        # Tests to ensure the correct user data definition passes
        data = {
            "username": "",
            "password": "nadra2526#A"
        }
        self.assertEqual(self.validation.validate_login(data['username'],data['password']), "Input username or password")
    
    def test_validate_login_empty_password(self):
        # Tests to ensure the correct user data definition passes
        data = {
            "username": "nadralia",
            "password": ""
        }
        self.assertEqual(self.validation.validate_login(data['username'],data['password']), "Input username or password")

    def test_if_its_a_validate_password(self):
        password = 'Nadra2922@'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Valid Password")
 
    def test_minimum_length_of_password(self):
        password = 'Nadra'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Minimum length of password: 6 and  Maximum length of password: 12")

    def test_maximum_length_of_password(self):
        password = 'Nadra2922@as2#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Minimum length of password: 6 and  Maximum length of password: 12")

    def test_lowercase_character(self):
        password = 'NADRA2922#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 lowercase character [a-z]")

    def test_uppercase_character(self):
        password = 'nadra2922#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 uppercase character [A-Z]")
    
    def test_number_character(self):
        password = 'Nadralia#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 number between [0-9]")
    
    def test_special_character(self):
        password = 'Nadra2922'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 character from [$#@]")