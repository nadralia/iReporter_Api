import re

class Validation:

    # add redflag validation.
    def redflag_validation(self, createdOn, createdBy, redflag_type, email, location, comment):
        if not location:
            return "location is missing"
        if not createdOn:
            return "the date is missing"
        if not createdBy:
            return "Owners name is missing"
        if not redflag_type:
            return "redflag type is missing"
        if not comment:
            return "comment is missing"
        if  not email:
            return "Email address is missing"
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            return "Invalid email format"

    def validate_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

    def validate_user(self, data):
        # Validates user fields
        user_fields = ['username', 'email', 'password', 'full_name',
                       'role', 'gender']
        try:
            if len(data.keys()) == 0:
                return "No user added"
            for user_field in user_fields:
                if data[user_field] == "":
                    return user_field + " cannot be blank"

            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                            data['email']):
                return "Invalid email format"

            if not re.match(r"([a-zA-Z ]*$)", data['full_name']):
                return "Only alphanumerics allowed in user's full name"

            if not re.match(r"([a-zA-Z0-9]*$)", data['username']):
                return "Only alphanumerics allowed in user name"

            if re.match(r"([0-9])", data['username']):
                return "user name cannot contain numbers only"

            if len(data['password']) < 5:
                return "Password too short"

            if data['gender'] != "female" and data['gender'] != "male":
                return "gender can only be female or male"

            if data['role'] != 'Admin' and data['role'] != 'Reporter':
                return "Role must be either Admin or Reporter"
            else:
                return "is_valid"
        except KeyError:
            return "Invalid, Key fields missing"

    def validate_login(self, data):
        try:
            if len(data.keys()) == 0 or len(data.keys()) > 2:
                return "Only email and password for login"
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