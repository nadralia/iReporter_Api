import re

class Validation:

    def redflag_validation(self, data):
        """ add redflag validation."""
        try:
            if data['email'] == " ":
                message = {"message":"Email is missing"}
            if data['comment'] == " ":
                message = {"message":"Comment of the redflag is missing"}
            if data['type'] == " ":
                message = {"message":"Type of redflag is missing"}
            if data['createdBy'] == " ":
                message = {"message":"Created by is missing"}
            if data['location'] == " ":
                message = {"message":"Created by is missing"}
            if len(data.keys()) == 0:
                message = {"message":"No redflag added"}
            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",data['email']):
                message = {"message":"Invalid email format"}
            else:
                message = "Valid"
            return message
        except KeyError:
            return "Invalid Key Fields"

    def validate_input_type(self, input):
        """check if the input values is an integer"""
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

    def validate_user(self, data):
        """ Validates user fields"""
        try:
            if len(data.keys()) == 0:
                message = {"message":"No user added"}

            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                            data['email']):
                message = {"message":"Invalid email format"}

            if not re.match(r"([a-zA-Z ]*$)", data['full_name']):
                message = {"message":"Only alphanumerics allowed in user's full name"}
            if not re.match(r"([a-zA-Z0-9]*$)", data['username']):
                message = {"message":"Only alphanumerics allowed in user name"}

            if re.match(r"([0-9])", data['username']):
                message = {"message":"user name cannot contain numbers only"}

            if len(data['password']) < 5:
                message = {"message":"Password too short"}

            if data['gender'] != "female" and data['gender'] != "male":
                message = {"message":"gender can only be female or male"}

            if data['role'] != 'Admin' and data['role'] != 'Reporter':
                message = {"message":"Role must be either Admin or Reporter"}
            else:
                message = "is_valid"
            return message
        except KeyError:
            return "Invalid, Key fields missing"

    def validate_login(self, data):
        try:
            if 'email' not in data.keys():
                return "Email is missing"
            if 'password' not in data.keys():
                return "Missing password"
            if data['email'] == "" or data['password'] == "":
                return "Input email or password"
            else:
                return "Credentials valid"
        except KeyError:
            return "Invalid fields"