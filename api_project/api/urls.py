from django.urls import path, include
#from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
   # path('book-list/', BookList.as_view(), name='book-list-view'),
    path('', include(router.urls)),
]