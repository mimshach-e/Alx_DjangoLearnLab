from django.shortcuts import redirect, get_object_or_404
from .models import CustomUser
from django.contrib.auth import login, authenticate
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CustomUserSerializer, LoginSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], 
                            password=serializer.validated_data['password'])
        login(request, user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileAPIView(views.APIView):
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# A view to follow a user only when logged-in
class FollowUser(views.APIView):
    permission_classes = [IsAuthenticated]

    def follow_user(self, request, pk):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        if request.user == user_to_follow:
            return Response({"error": "You can't follow yourself"}, status=400)
        request.user.following.add(user_to_follow)




# A view to unfollow a user only when logged-in
class UnfollowUser(views.APIView):
    permission_classes = [IsAuthenticated]

    def unfollow_user(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if request.user == user_to_unfollow:
            return Response({"error": "You can't unfollow yourself"}, status=400)
        request.user.following.remove(user_to_unfollow)

