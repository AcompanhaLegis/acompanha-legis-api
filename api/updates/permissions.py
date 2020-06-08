from rest_framework import permissions


class IsSubscriptionOwner(permissions.BasePermission):
    """
        Permission to change subscription.
    """
    def has_object_permissions(self, request, view, obj):
        return obj.user == request.user
