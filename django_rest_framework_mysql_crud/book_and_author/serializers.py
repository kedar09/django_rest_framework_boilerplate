from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_name', 'author_email', 'author_contact')


class BookSerializer(serializers.ModelSerializer):
    # author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    author_id = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ('book_id', 'book_name', 'author_id')