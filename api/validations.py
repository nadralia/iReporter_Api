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