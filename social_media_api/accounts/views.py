from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, LoginSerializer, TokenSerializer


# A view for registering a new user
class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # creating a token for the newly registered user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': CustomUserSerializer(user).data}, status=status.HTTP_201_CREATED)

# A view to login in a user
class LoginAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)

        # create or retrieve a token for logged-in user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


# A view for user profile management
class ProfileAPIView(views.APIView):
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# A view for retrieving token
class TokenAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
