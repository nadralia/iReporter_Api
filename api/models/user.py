class User(object):
    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.full_name = kwargs['full_name']
        self.email = kwargs['email']
        self.gender = kwargs['gender']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.role = kwargs['role']
