from rest_framework import viewsets, permissions

from metrics.permissions import IsAppOrReadOnly
from metrics.models import DeputadoMetrics
from metrics.serializers import DeputadoMetricsSerializer


class DeputadoMetricsViewSet(viewsets.ModelViewSet):
    """
        API endpoints for deputado metrics management
    """
    queryset = DeputadoMetrics.objects.all()
    serializer_class = DeputadoMetricsSerializer 
    permission_classes = [permissions.IsAuthenticated, IsAppOrReadOnly]
