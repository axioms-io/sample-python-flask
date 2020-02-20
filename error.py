# Define error handler for token and scope errors
class AxiomsError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code