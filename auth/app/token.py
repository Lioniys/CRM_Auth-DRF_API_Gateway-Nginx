from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['company'] = user.info.company.pk
        token['is_paid_for'] = user.info.company.is_paid_for
        token['is_owner'] = user.info.in_owner
        return token
