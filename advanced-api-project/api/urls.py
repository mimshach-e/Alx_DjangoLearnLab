from django.urls import path
from .views import (
    ListView, DetailView, CreateView, 
    CreateAuthorView, UpdateView, DeleteView
)

urlpatterns = [
    path("book/", ListView.as_view(), name="book-list"),
    path("book/<int:pk>/", DetailView.as_view(), name="book-details"),
    path("author/create/", CreateAuthorView.as_view(), name="book-create"),
    path("book/create/", CreateView.as_view(), name="book-create"),
    path("book/update/<int:pk>/", UpdateView.as_view(), name="book-update"),
    path("book/delete/<int:pk>/", DeleteView.as_view(), name="book-delete"),
]

