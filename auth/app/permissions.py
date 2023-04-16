from rest_framework import permissions


class IsOwnerAndIsPaidFor(permissions.BasePermission):
    def has_permission(self, request, view):
        is_paid_for = request.auth.payload.get("is_paid_for", False)
        is_owner = request.auth.payload.get("is_owner", False)
        return bool(is_owner and is_paid_for)
