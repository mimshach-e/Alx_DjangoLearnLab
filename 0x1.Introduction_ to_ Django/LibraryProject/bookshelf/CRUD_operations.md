# importing the Book class from the bookshelf app model
from bookshelf.models import Book

# creating a new instance of the book class
>>> new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# saving the book instance
>>> new_book.save()

# verifying expected outputs
>>> new_book.id
4

>>> new_book.title
'1984'

>>> new_book.publication_year
1949


# retrieving and all the attributes of the book created
>>> Book.objects.all()
<QuerySet [<Book:  1984 by George Orwell, 1994>]>

# retrieving by id 
>>> Book.objects.filter(id=1)
<QuerySet [<Book:  1984 by George Orwell, 1994>]>

# retrieving by title 
>>> Book.objects.filter(title__startswith="198")
<QuerySet [<Book:  1984 by George Orwell, 1949>]>

# retrieving by author 
>>> Book.objects.filter(author__startswith="George")
<QuerySet [<Book:  1984 by George Orwell, 1949>]>

# retrieving by publication year 
>>> Book.objects.filter(publication_year__startswith="194")
<QuerySet [<Book:  1984 by George Orwell, 1949>]>


# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

>>> new_book.title = "Nineteen Eighty-Four"
>>> new_book.save()

# expected output
>>> new_book.title
'Nineteen Eighty-Four'


# Delete the book you created and confirm the deletion by trying to retrieve all books again.
>>> new_book.delete()
(1, {'bookshelf.Book': 1})

# verifying output
>>> Book.objects.all()  
<QuerySet []>