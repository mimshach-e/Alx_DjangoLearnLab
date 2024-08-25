from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f" {self.title} by {self.author}, {self.publication_year}"
    
# Creating a custom user using AbtractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank= False, null=False, editable=True)
    profile_photo = models.ImageField(blank=True, null=True, editable=True)

# Integrate the Custom User Model into Admin
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        if not username:
            raise ValueError("You must have a username")
        if not email:
            raise ValueError("You must have an email address")
        
        user = self.model(
            username=username, 
            email=self.normalize_email(email), 
            date_of_birth=date_of_birth
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None):
        user = self.create_user(
            username = username, 
            email = email, 
            date_of_birth = date_of_birth, 
            password = password
            )
        
        user.is_admin = True
        user.save(using=self._db)
        return user



