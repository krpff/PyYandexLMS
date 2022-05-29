class AuthError(Exception):
    pass


class ApiError(Exception):
    def __init__(self, message, *args):
        self.message = message
        super(ApiError, self).__init__(message, *args)
