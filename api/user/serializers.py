from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):
        self.reset_form = PasswordResetForm(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)
        return value

    def save(self):
        request = self.context.get('request')
        self.reset_form.save(
            use_https=request.is_secure(),
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL'),
            request=request,
        )


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        self._errors = {}

        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({'uid': ['Valor invalido']})

        self.set_password_form = SetPasswordForm(user=self.user, data=attrs)
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Valor invalido']})

        return attrs

    def save(self):
        return self.set_password_form.save()
