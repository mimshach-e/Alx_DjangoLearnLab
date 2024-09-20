from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework


# Create Views for CRUD Operations

# Custom permission to only allow authors of an object to edit or delete it.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of the post/comment
        return obj.author == request.user

    

# Post view
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']
    pagination_class = PageNumberPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# Comment view
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

# A Feed view to display posts of following users 
class FeedView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the list of all users the current user is following
        following_users = self.request.user.following.all()

        # Retrieve post from the users the current user is following, ordering by most recent date created
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
