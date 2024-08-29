from django.urls import path
from .views import BookList

urlpatterns = [
    path('book-list/', BookList.as_view(), name='book-list-view'),
]