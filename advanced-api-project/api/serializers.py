# Importing necessary modules and classes
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# A Serializer class to serialize the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year must not be in the future.')
        return value
    

# A Serializer class to serialize the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # A nested BookSerializer to serialize the related books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
    
    
