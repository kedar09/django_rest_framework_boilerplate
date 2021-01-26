from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_name', 'author_email', 'author_contact')
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        # fields = ('book_id', 'book_name', 'authors')
        fields = ('__all__')
        depth = 1
