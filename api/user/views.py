from django.contrib.auth import get_user_model
from rest_framework import views, status, authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.permissions import IsOwner
from user.serializers import (UserSerializer, NewUserSerializer,
                              ChangePasswordSerializer,
                              PasswordResetSerializer,
                              PasswordResetConfirmSerializer)


User = get_user_model()

class RegisterView(views.APIView):
    """
        API endpoint that allows users to be created.
    """
    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(views.APIView):
    """
        API endpoint that allows users to change their password
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if request.data['password'] != request.data['confirm_password']:
            return Response('Senhas nāo coincidem', status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'OK'})
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(views.APIView):
    """
        API endpoint that allows users to request a password reset.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data,
                                             context={'request': request})
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({"detail": "Password reset e-mail has been sent."},
                        status=status.HTTP_200_OK)


class PasswordResetConfirmView(views.APIView):
    """
        API endpoint that allows users with a valid token to reset their
        passwords.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": 'Password has been reset with the new password.'}
        )


class ProfileView(views.APIView):
    """
        API endpoint that allows users to see and change their profile
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def get(self, request):
        user = request.user 
        serializer = UserSerializer(user, context={ 'request': request })
        return Response({ 'user': serializer.data })

    def patch(self, request):
        serializer = UserSerializer(data=request.data, partial=True)
        if user and serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
