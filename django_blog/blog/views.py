from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Post
from .forms import CustomRegistrationForm, UserProfileForm


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
    return render(request, 'registration/register.html', {'form': form})        


# Profile View and Management 
"""
The Profile view displays the user's name and 
allows for updating email address
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
    return render(request, 'registration/profile.html', {'form': form})
    
 

def homeView(request):
    return render(request, 'blog/home.html')   


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})