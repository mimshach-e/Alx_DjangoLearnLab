from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
