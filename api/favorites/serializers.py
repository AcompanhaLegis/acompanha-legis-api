from rest_framework import serializers

from favorites.models import FavoriteProposicao, FavoriteDeputado


class FavoriteProposicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProposicao
        fields = '__all__'

class FavoriteDeputadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProposicao
        fields = '__all__'
