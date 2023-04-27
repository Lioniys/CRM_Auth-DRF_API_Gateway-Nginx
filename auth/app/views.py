from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerAndIsPaidFor


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def verify_view():
    return Response(status=200)


# self.request.auth.payload.get("user_id")
# self.request.auth.payload.get("company")
# self.request.auth.payload.get("is_paid_for")
# self.request.auth.payload.get("is_owner")
