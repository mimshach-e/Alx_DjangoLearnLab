# importing the Book class from the bookshelf app model
from bookshelf.models import Book

# creating a new instance of the book class
>>> new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# saving the book instance
>>> new_book.save()

# verifying expected outputs
>>> new_book.id
6

>>> new_book.title
'1984'

>>> new_book.publication_year
1949

>>> Book.objects.all()
<QuerySet [<Book:  1984 by George Orwell, 1994>]>

