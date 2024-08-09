# retrieving and all the attributes of the book created
>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book:  1984 by George Orwell, 1994>]>

# retrieving by id 
>>> Book.objects.get(id=6) 
<Book:  1984 by George Orwell, 1949>

# retrieving by title 
>>> Book.objects.get(title="1984")
<Book:  1984 by George Orwell, 1949>

# retrieving by author 
>>> Book.objects.get(author__startswith="George")
<Book:  1984 by George Orwell, 1949>

# retrieving by publication year 
>>> Book.objects.get(publication_year__startswith=194)      
<Book:  1984 by George Orwell, 1949>