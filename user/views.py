from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from user.serializers import RegisterSerializer, LoginSerializer
from user import models


class LoginView(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        user_login = models.UserLogin.objects.all().order_by("-attempted_at")
        serializer = LoginSerializer(user_login, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_login = models.UserLogin(username=serializer.validated_data['user'])
        user_login.save()
        return Response({'token': token.key})


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data = {**serializer.data, "token": token}
        else:
            data = serializer.errors

        return Response(data)
