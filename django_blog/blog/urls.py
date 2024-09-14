from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import registerView, profileView, homeView, post_list

urlpatterns = [
    path('register/', registerView, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profileView, name='profile'),
    path('', homeView, name='home'), 
    path('posts/', post_list, name='posts'),
]