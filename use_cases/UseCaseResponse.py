class UseCaseResponse:
    __BAD_RESPONSE_TYPES = (str, None)

    def __init__(self, data):
        self.__data = data

    def is_success(self):
        return type(self.__data) not in self.__BAD_RESPONSE_TYPES

    def get_response(self):
        return self.__data
