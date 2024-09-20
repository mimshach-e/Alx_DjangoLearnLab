from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, FeedView
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)
router.register(r'feed', FeedView, basename='feed')

urlpatterns = [
    path('', include(router.urls))
]