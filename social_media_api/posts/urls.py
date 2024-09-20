from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, FeedView
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='posts-feed'),
]