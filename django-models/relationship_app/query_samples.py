from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author = Author.objects.get(id=1)
all_books_by_author = author.books.all()

print("All Books by the author:")
for book in all_books_by_author:
    print(book.title)

# List all books in a library.
library = Library.objects.get(id=1)
all_books_in_library = library.books.all()

print("All Books in the Library")
for book in all_books_in_library:
    print(book.title)

# Retrieve the librarian for a library.
library = Library.objects.get(id=1)
librarian = library.librarian

print(f"The Librarian for the library is: {librarian.name}")