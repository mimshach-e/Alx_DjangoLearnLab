from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return f" {self.title} by {self.author}, {self.publication_year}"
    
    class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]



# Create User Manager for Custom User Model
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



# Creating a custom user using AbtractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank= False, null=False, editable=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True, editable=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)

    # Linking the custom manager to the CustomUser model
    objects = CustomUserManager() 

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email'] 

    def __str__(self):
        return self.username


