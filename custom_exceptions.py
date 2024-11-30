
__author__ = "Chirag Kamble"


class CustomException(Exception):
    """
    Custom exception for specific errors in the program.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
