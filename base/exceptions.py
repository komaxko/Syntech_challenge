from rest_framework.exceptions import APIException


class ValidationError(APIException):
    status_code = 400
    default_detail = 'Validation error'


class AlreadyExists(APIException):
    status_code = 409
    default_detail = 'such object already exists'
