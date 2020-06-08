from django.contrib.auth import get_user_model
from rest_framework import views, status, authentication, permissions
from rest_framework.response import Response
from user.serializers import UserSerializer, NewUserSerializer, ResetPasswordSerializer

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


class ResetPasswordView(views.APIView):
    """
        API endpoint that allows users to change their password
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        user = request.user
        serializer = ResetPasswordSerializer(data=request.data)
        if data['password'] != data['confirm_password']:
            return Response('Senhas nāo coincidem', status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'OK'})
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ProfileView(views.APIView):
    """
        API endpoint that allows users to see and change their profile
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        user = request.user 
        serializer = UserSerializer(user, context={ 'request': request })
        return Response({ 'user': serializer.data })

    def patch(self, request):
        serializer = UserSerializer(data=request.data, partial=True)
        if user and serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
