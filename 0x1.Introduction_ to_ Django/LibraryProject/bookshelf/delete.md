>>> from bookshelf.models import Book
# Delete the book you created and confirm the deletion by trying to retrieve all books again.
>>> new_book.delete()
(1, {'bookshelf.Book': 1})

# verifying output
>>> Book.objects.all()  
<QuerySet []>