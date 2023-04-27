from rest_framework.exceptions import APIException


class TokenException(APIException):
    status_code = 401
    default_detail = 'Unable to generate an access token.'
    default_code = 'token_error'
