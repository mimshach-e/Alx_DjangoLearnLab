from django.urls import path
from .views import ListView

urlpatterns = [
    path('book/', ListView.as_view(), name="book-list"),
]

