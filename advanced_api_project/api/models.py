from django.db import models

# Create your models here.

# A class model for the Author of a book
class Author(models.Model):
    name = models.CharField(max_length=100)

# A class model for the Book
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
