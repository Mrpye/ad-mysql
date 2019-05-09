"""Module for Error classes. """
class MySqlError(Exception):
    """Template Error class. """

    def __init__(self, status_code, http_error_text, response):
        super(MySqlError, self).__init__(http_error_text)
        self.status_code = status_code
        self.response = response
