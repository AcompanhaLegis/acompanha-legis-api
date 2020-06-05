from rest_framework import permissions


class IsAppOrReadOnly(permissions.BasePermission):
    """
        Permission to change subscription.
    """
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_app
