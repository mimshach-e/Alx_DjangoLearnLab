from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Post, Comment
from .forms import CustomRegistrationForm, UserProfileForm, PostCreateForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
def tagged_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'tag_posts.html', {'tag': tag, 'posts': posts})

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, 'search_results.html', {'posts': posts, 'query': query})    
    
    
# Create View: This view allows authenticated users or authors to create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class =PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully.')
        return super().form_valid(form)


# Post Update View to allow authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_update.html'
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
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

# IMPLEMENTING COMMENT VIEWS FOR THE BLOG POST
"""
A view to add comments to a blog post.
"""
class CommentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
   

"""
A view to update comments on a blog post.
"""
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'

    # this gives a dynamic direction back to the post detail view after successful update 
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    # this ensures that the only the update comments
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
