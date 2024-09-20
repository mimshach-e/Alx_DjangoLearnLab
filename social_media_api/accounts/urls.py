from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, FollowUser, UnfollowUser

urlpatterns = [
    # Account URLs
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),

    #Follow URLs
    path('follow/<int:pk>/', FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUser.as_view(), name='unfollow-user'),
]
