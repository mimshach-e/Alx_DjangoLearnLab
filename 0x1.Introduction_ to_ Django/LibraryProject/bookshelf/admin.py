from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author__name")
    

# grouping fields in the book form using fieldsets
    fieldsets = (
    (None, {
        'fields': ('title', 'author')
    }),
    ('Additional Info', {
        'fields': ('publication_year', 'isbn')
    }),
)
    
admin.site.register(Book, BookAdmin)

