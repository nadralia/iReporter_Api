from flask import request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from api.helpers.utils import is_empty
import uuid
import jwt
from datetime import datetime, timedelta
from api.validations import Validation
from config import Config

validation_obj = Validation()

users = []

class User:
    def __init__(self, **kwargs):
        """ stores user details """
        self.user_id = kwargs.get('user_id')
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.email = kwargs.get('email')
        self.gender = kwargs.get('gender')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.registered = kwargs.get('registered')
        self.is_admin = False

    def create_user(self):
        return {
            "user_id": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "gender": self.gender,
            "password": self.password,
            "username": self.username,
            "registered": self.registered,
            "isAdmin": self.is_admin,
        }

    
    def register_user(self):
        """ allows store owner to register new users """
        data = request.get_json()
        search_keys = ("firstname", "lastname", "email", "username", 
        "password", "gender", "role")
        if all(key in data.keys() for key in search_keys):
            email = data.get("email")
            username = data.get("username")
            firstname = data.get("firstname")
            lastname = data.get("lastname")
            gender = data.get("gender")
            password = data.get("password")
            
            is_valid = validation_obj.validate_user(username,email,gender)             
            valid_password = validation_obj.validate_password(password)
            if is_valid == "is_valid":
                user_id = uuid.uuid4().int
                registered = datetime.now()
                if valid_password == "Valid Password":
                    hashed_password = generate_password_hash(password, method='sha256')
                    response = None

                    new_user = User(user_id=user_id, firstname=firstname, 
                    lastname=lastname, email=email,
                    gender=gender, username=username,password=hashed_password, 
                    registered=registered,
                    is_admin=self.is_admin)

                    already_registered = [user for user in users if user['username']==username]
                    if is_empty(already_registered):
                        users.append(dict(new_user.__dict__))
                        response = {"status": 201, "message":"User registered successfully"}
                        print(users)
                    else:
                        response = {'error':'User with that username already exists'}
                    return response
                response = {"message": valid_password}
                return response
            response = {"message": is_valid}
            return response
        response = {"message": "a 'key(s)' is missing in your request body"}
        return response

    def get_users(self):
        """Fetch all users """
        if is_empty(users):
            response = {'message': 'No registered users at the moment.'}
        else:
            response = users
        return response

    def get_user_details(self, username, password):
        for user in users:
            if user['username'] == username and check_password_hash(
                    user['password'], password
            ):
                return user
        return "User does not exist"



