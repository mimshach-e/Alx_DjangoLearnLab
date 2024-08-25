from django.contrib import admin
from .models import Book
from django.contrib.admin import UserAdmin
from .models import CustomUser, CustomUserManager

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author__name")
    
admin.site.register(Book, BookAdmin)

# Integrate the Custom User Model into Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')})
        )
admin.site.register(CustomUser, CustomUserAdmin)    

class CustomUserMangerAdmin(admin.ModelAdmin):
    model = CustomUserManager
    fields = ["username", "email", "date_of_birth", "password"]
admin.site.register(CustomUserManager, CustomUserMangerAdmin)






