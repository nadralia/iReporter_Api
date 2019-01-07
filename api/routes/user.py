from flask import request, jsonify, Blueprint
from api.validations import Validation
from api.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
from config import Config
import jwt
import re

user = Blueprint('user', __name__)

users = []
created_token = []

validation_obj = Validation()

"""Helper functions"""
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"message": "Missing Token"}), 403
        try:
            data_token = jwt.decode(token, Config.SECRET_KEY)
            created_token.append(data_token)
        except:
            return jsonify({"message": "Invalid token"}), 403
        return f(*args, **kwargs)
    return decorated

def assigns_token(data):
    for user in users:
        if user.email == data['email'] and\
           check_password_hash(user.password, data['password']):
                token = jwt.encode({'user': user.username,
                                    'exp': datetime.utcnow() +
                                    timedelta(minutes=30),
                                    'roles': user.role},
                                   Config.SECRET_KEY)
                return jsonify({'token': token.decode('UTF-8')}), 200
    return jsonify({
        "message": "User either not registered or forgot password"}), 400

"""User Views/Routes"""
@user.route('/api/v1/users', methods=['POST'])
def register_user():
    """ registers a user"""
    data = request.get_json()
    role = data.get("role")
    email = data.get("email")
    username = data.get("username")
    
    is_valid = validation_obj.validate_user(username,email,role)
    for user in users:
        if user.email == data['email']:
            return jsonify({"message": "user already exists!"}), 400
    try:
        if is_valid == "is_valid":
            user_id = len(users)
            user_id += 1
            hashed_password = generate_password_hash(data['password'], method='sha256')
            kwargs = {
                "user_id": user_id,
                "full_name": data['full_name'],
                "email": data['email'],
                "gender": data['gender'],
                "username": data['username'],
                "password": hashed_password,
                "role": data['role']
            }
            user = User(**kwargs)
            users.append(user)
            return jsonify({"message":"User registered successfully"}), 201
        return jsonify({"message": is_valid}), 400
    except KeyError:
        return "Invalid key fields"

@user.route('/api/v1/login', methods=['POST'])
def login():
    """Logs in a user"""
    data = request.get_json()
    try:
        username = data.get("username")
        password = data.get("password")
        is_valid = validation_obj.validate_login(username, password)
        if is_valid == "Credentials valid":
            return assigns_token(data)
        return jsonify({"message": is_valid}), 400
    except KeyError:
        return jsonify({"message": "Invalid keys"}), 400

