from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerAndIsPaidFor

# self.request.auth.payload.get("user_id")
# self.request.auth.payload.get("company")
# self.request.auth.payload.get("is_paid_for")
# self.request.auth.payload.get("is_owner")


class Test(APIView):
    permission_classes = (IsAuthenticated, IsOwnerAndIsPaidFor)

    def get(self, request):
        a = self.request.auth.payload.get("user_id")
        x = self.request.auth.payload.get("company")
        z = self.request.auth.payload.get("is_paid_for")
        c = self.request.auth.payload.get("is_owner")
        return Response({"count": [a,x,z,c]})
