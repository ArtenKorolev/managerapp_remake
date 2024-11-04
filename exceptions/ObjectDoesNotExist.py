class ObjectDoesNotExist(Exception):
    def __init__(self, error_message):
        self.__error = error_message

    def what(self):
        return self.__error
