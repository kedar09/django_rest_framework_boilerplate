from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_name', 'author_email', 'author_contact')


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())


    class Meta:
        model = Book
        fields = ('book_id', 'book_name', 'authors')
        # fields = ('__all__')
        depth = 1

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('authors')
    #     book = Book.objects.create(**validated_data)
    #     for author_data in authors_data:
    #         Author.objects.create(book=book, **authors_data)
    #     return book
