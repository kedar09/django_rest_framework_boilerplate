from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from django.http import Http404
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import status
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def add_get_authors(request):
    if request.method == 'GET':
        author_list = Author.objects.all()
        author_list_serializer = AuthorSerializer(author_list, many=True)
        # return JsonResponse({"message": "success", "status": 200, "response": author_list_serializer.data})
        return Response(author_list_serializer.data)

    elif request.method == 'POST':
        add_author_serializer = AuthorSerializer(data=request.data)
        if add_author_serializer.is_valid():
            add_author_serializer.save()
            return Response(add_author_serializer.data, status=status.HTTP_201_CREATED)
        return Response(add_author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_author_by_id(request, pk):
    try:
        author_details = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        author_details_serializer = AuthorSerializer(author_details)
        return Response(author_details_serializer.data)

    elif request.method == 'PUT':
        update_author_serializer = AuthorSerializer(
            author_details, data=request.data)
        if update_author_serializer.is_valid():
            update_author_serializer.save()
            return Response(update_author_serializer.data, status=status.HTTP_200_OK)
        return Response(update_author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print('called')
        author_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def add_get_books(request):
    if request.method == 'GET':
        books_and_authors_list = Book.objects.all()
        books_and_authors_list_serializer = BookSerializer(
            books_and_authors_list, many=True)
        return Response(books_and_authors_list_serializer.data)

    elif request.method == 'POST':
        try:
            author_details = Author.objects.get(pk=request.data['author_id'])
        
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        book = {
            'book_name': request.data['book_name'],
            'author_id': author_details
        }
        add_book_serializer = BookSerializer(data=book)

        if add_book_serializer.is_valid():
            print(add_book_serializer.validated_data)
            add_book_serializer.create(validated_data=book)
            return Response(add_book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(add_book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_add_update_book_by_id(request, pk):
    try:
        book_and_author_details = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        book_and_author_details_serializer = BookSerializer(
            book_and_author_details)
        return Response(book_and_author_details_serializer.data)

    elif request.method == 'PUT':
        update_book_serializer = BookSerializer(book_and_author_details, data=request.data)
        if update_book_serializer.is_valid():
            update_book_serializer.save()
            return Response(update_book_serializer.data, status=status.HTTP_200_OK)
        return Response(update_book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book_and_author_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
