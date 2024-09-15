from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import CustomRegistrationForm, UserProfileForm, CreatePostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Registration View
def registerView(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect(reverse('home'))
    else:
        form = CustomRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})        


# Profile View and Management 
"""
The Profile view displays the fist and last name, and email address of the user 
and as well allows for updating them. The profile view can only be accessed when
logged in.
"""
@login_required
def profileView(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})
    
 
# This the hompage view
def homeView(request):
    return render(request, 'blog/home.html')   


# List View: This view allows you to view the list of all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# Detail View: This view displays full details of each post by ID
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
# Create View: This view allows authenticated users or authors to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class =CreatePostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully.')
        return super().form_valid(form)


# Post Update View to allow authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/update_post.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post updated successfully.')
        return super().form_valid(form)
    
    # Only allow the author of the post to edit it
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete View: This view allows authenticated users or authors to delete posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    



