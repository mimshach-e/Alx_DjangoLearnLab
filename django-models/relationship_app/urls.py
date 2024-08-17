from django.urls import path
from .views import list_books, LibraryDetailView #custom_logout_view
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    #path('logout/', custom_logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', TemplateView.as_view(template_name = 'relationship_app/profile.html'), name='profile'),
]

