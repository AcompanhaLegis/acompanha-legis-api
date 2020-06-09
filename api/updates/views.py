from rest_framework import viewsets, permissions

from api.permissions import IsOwner

from updates.models import UpdateSubscription
from updates.serializers import UpdateSubscriptionSerializer


class UpdateSubscriptionViewSet(viewsets.ModelViewSet):
    """
        API endpoints for subscription management
    """
    queryset = UpdateSubscription.objects.all()
    serializer_class = UpdateSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
