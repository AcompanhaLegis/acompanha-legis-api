from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
        Permission to object which the request user is the owner.
    """
    def has_object_permissions(self, request, view, obj):
        return obj.user == request.user
