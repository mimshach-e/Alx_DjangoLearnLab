from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.

def all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)

        print(f"All Books by {author_name}:")

        for book in books:
            print(f"- {book.title}")

    except Author.DoesNotExist:
        print(f"No author is found with the name {author_name}")

# List all books in a library.
def all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Book.objects.filter(library=library)

        print(f"All Books in {library_name}:")

        for book in books:
            print(f"- {book.title}")

    except Library.DoesNotExist:
        print(f"No library is found with the name {library_name}")

# Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The Librarian for {library_name} is {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library {library_name}")

# Example usage
if __name__ == "__main__":
    all_books_by_author("Brian Tracy")         
    all_books_in_library("Ghana Library")      
    get_librarian_for_library("Mercy Elson")
