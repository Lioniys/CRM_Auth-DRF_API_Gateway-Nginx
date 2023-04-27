from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import TokenException


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        try:
            token = super().get_token(user)
            token['company'] = user.info.company.pk
            token['is_paid_for'] = user.info.company.is_paid_for
            token['is_owner'] = user.info.in_owner
        except ObjectDoesNotExist:
            raise TokenException()
        return token
