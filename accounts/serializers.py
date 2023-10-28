from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
##연습용 Serializer
from rest_framework.serializers import ModelSerializer
from datetime import datetime

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

class CustomLoginSerializer(LoginSerializer):
    # email 필드를 제거
    email = None
