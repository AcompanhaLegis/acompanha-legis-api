from django.contrib.auth import get_user_model
from rest_framework import serializers

from favorites.serializers import FavoriteProposicaoSerializer, FavoriteDeputadoSerializer
from updates.serializers import UpdateSubscriptionSerializer

User = get_user_model()


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Overriding method for password hashing."""
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    favorite_proposicoes = FavoriteProposicaoSerializer(many=True, read_only=True)
    favorite_deputados = FavoriteDeputadoSerializer(many=True, read_only=True)
    subscriptions = UpdateSubscriptionSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
                'id',
                'email',
                'is_active',
                'valid_until',
                'favorite_proposicoes',
                'favorite_deputados',
                'subscriptions',
                ]
        read_only_fields = ['is_active', 'valid_until']


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
