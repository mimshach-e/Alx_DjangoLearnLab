from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

# A Registration serializer to serialize the CustomUser model for registration
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
            return make_password(value)

    def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            return user
        

# A Login serializer 
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active():
            return user
        raise serializers.ValidationError("Invalid Credentials")  

# # A serializer for the token retrieval 
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key'] 




