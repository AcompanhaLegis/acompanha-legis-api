from rest_framework import viewsets, permissions

from api.permissions import IsOwner

from favorites.models import FavoriteProposicao, FavoriteDeputado
from favorites.serializers import FavoriteProposicaoSerializer, FavoriteDeputadoSerializer


class FavoriteProposicaoViewSet(viewsets.ModelViewSet):
    """
        API endpoints for favorite proposicao management
    """
    queryset = FavoriteProposicao.objects.all()
    serializer_class = FavoriteProposicaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class FavoriteDeputadoViewSet(viewsets.ModelViewSet):
    """
        API endpoints for favorite deputado management
    """
    queryset = FavoriteDeputado.objects.all()
    serializer_class = FavoriteDeputadoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
