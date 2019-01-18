from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from api.helpers.token import generate_token
from flask.views import MethodView
import datetime
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from api.models.user import User
from api.validations import Validation

validation_obj = Validation()
user_obj = User()
user_blueprint = Blueprint("user_blueprint", __name__)

admin_user = User(user_id=1, firstname='adralia', lastname='nelson', email='nadralia@gmail.com',
        gender='Male', username='nadralia',password='nadra24T#', 
        registered='Sat, 22 Dec 2018 11:42:19 GMT', is_admin=True)

reporter   = User(user_id=2, firstname='adralia', lastname='amos', email='adraliaamos@gmail.com',
        gender='Male', username='aamos2922',password='nadra24T#', 
        registered='Sat, 22 Dec 2018 11:42:19 GMT', is_admin=False)

class RegisterUser(MethodView):
    def post(self):
        response = user_obj.register_user()
        return jsonify(response)
       

registration_view = RegisterUser.as_view("registration_view")
user_blueprint.add_url_rule("/api/v1/auth/signup",view_func=registration_view, methods=["POST"])

class Login(MethodView):
    def post(self):
        """ login function """
        user_data = request.get_json()
        search_keys = ("username", "password")
        if all(key in user_data.keys() for key in search_keys):
            try:

                username = user_data.get("username")
                password = user_data.get("password")
                is_valid = validation_obj.validate_login(username, password)
                if is_valid == "Credentials valid":
                    # get user datails
                    data = user_obj.get_user_details(username, password)
                    print(data)
                    response = (
                        jsonify(
                            {
                                "status": 200,
                                "data": [
                                    {
                                        "token": generate_token(
                                            data['user_id'], data['is_admin']
                                        ),
                                        "message": "Logged in successfully",
                                    }
                                ],
                            }
                        ),
                        200,
                    )

                    return response

                return jsonify({"message": is_valid}), 400  
            except KeyError:
                response = (
                    jsonify(
                        {
                            "error": "Please provide the correct keys for the data",
                            "status": 422,
                        }
                    ),
                    422,
                )
            return response
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400


        

login_view = Login.as_view("login_view")
user_blueprint.add_url_rule("/api/v1/auth/login",view_func=login_view, methods=["POST"])


