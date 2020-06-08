from rest_framework import viewsets, permissions
from rest_framework.response import Response

from updates.models import UpdateSubscription
from updates.serializers import UpdateSubscriptionSerializer
from updates.permissions import IsSubscriptionOwner


class UpdateSubscriptionViewSet(viewsets.ModelViewSet):
    """
        API endpoints for subscription management
    """
    queryset = UpdateSubscription.objects.all()
    serializer_class = UpdateSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsSubscriptionOwner]
