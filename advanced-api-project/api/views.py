from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


# Create your views here.

# Implementing a List API view for the Book Model
class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer