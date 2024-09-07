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

# Implementing a Detail API view for the Book Model
class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer
    lookup_field = "pk"

# Implementing a Create API view for the Author Model
class CreateAuthorView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Implementing a Create API view for the Book Model
class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    


class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer