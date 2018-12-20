class Validation:

    # add redflag validation.
    def redflag_validation(self, createdOn, createdBy, redflag_type, email, location):
        if not location:
            return "location is missing"
        if email == " ":
            return "Email address is missing"

    def validate_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"