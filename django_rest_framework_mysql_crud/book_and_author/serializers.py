from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_name','author_email', 'author_contact')

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ('book_id','book_name', 'author')
        # fields = ('__all__');