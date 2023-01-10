from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import UserLogin


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise ValidationError({'error': 'Passwords are not same'})

        if User.objects.filter(email=email).exists():
            raise ValidationError({'error': f"{email} is already registered"})

        account = User(username=username, email=email)
        account.set_password(password1)
        account.save()

        return account


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserLogin
        fields = "__all__"
