# retrieving and all the attributes of the book created
>>> from bookshelf.models import Book
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