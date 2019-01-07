import re

class Validation:

    def redflag_validation(self,comment,location, redflag_type):
        """ add redflag validation."""

        if comment == " ":
            message = {"message":"Comment of the redflag is missing"}
        if redflag_type == " ":
            message = {"message":"Type of redflag is missing"}
        if location == " ":
            message = {"message":"Created by is missing"}
        else:
            message = "Valid"
        return message

    def validate_input_type(self, input):
        """check if the input values is an integer"""
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

    def validate_user(self, username, password, email,role):
        """ Validates user fields"""
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",email):
            message = {"message":"Invalid email format"}
        if not re.match(r"([a-zA-Z0-9]*$)", username):
            message = {"message":"Only alphanumerics allowed in user name"}
        if len(password) < 5:
            message = {"message":"Password too short"}
        if role != 'Admin' and role != 'Reporter':
            message = {"message":"Role must be either Admin or Reporter"}
        else:
            message = "is_valid"
        return message

    def validate_login(self, username, password):
        try:

            if username == "" or password == "":
                return "Input username or password"
            else:
                return "Credentials valid"
        except KeyError:
            return "Invalid fields"