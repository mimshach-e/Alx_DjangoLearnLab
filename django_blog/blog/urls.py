from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import registerView, profileView, homeView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', registerView, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', profileView, name='profile'),
    path('', homeView, name='home'), 
    path('posts/', PostListView.as_view(template_name='blog/post_list.html'), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(template_name='blog/post_detail.html'), name='post_detail'),
    path('post/new/', PostCreateView.as_view(template_name='blog/create_post.html'), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='blog/update_post.html'), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='blog/delete_post.html'), name='post_delete'),
]