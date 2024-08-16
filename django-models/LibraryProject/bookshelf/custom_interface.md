## Integrating the Book Model with Django Admin

### Step 1: Register the Book Model
Registered the `Book` model in the `admin.py` file to enable admin functionality.

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author__name')
