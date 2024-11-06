class APIError(Exception):
    '''Базовый класс для исключений, связанных с API.'''

    def __init__(self, message, status_code=None, response_data=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data


class BadRequestError(APIError):
    '''Исключение для ошибки 400 Bad Request.'''

    pass


class UnauthorizedError(APIError):
    '''Исключение для ошибки 401 Unauthorized.'''

    pass


class ForbiddenError(APIError):
    '''Исключение для ошибки 403 Forbidden.'''

    pass


class NotFoundError(APIError):
    '''Исключение для ошибки 404 Not Found.'''

    pass


class UnprocessableEntityError(APIError):
    '''Исключение для ошибки 422 Unprocessable Entity.'''

    pass
