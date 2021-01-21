from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from django.http import Http404
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import status


@api_view(['GET'])
def getAuthors(request):
    author_list = Author.objects.all()
    author_list_serializer = AuthorSerializer(author_list, many=True)
    # return JsonResponse({"message": "success", "status": 200, "response": author_list_serializer.data})
    return Response(author_list_serializer.data)


@api_view(['GET'])
def getAuthorById(request, pk):
    try:
        author_details = Author.objects.get(pk=pk)
        author_details_serializer = AuthorSerializer(author_details)
        return Response(author_details_serializer.data)

    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def getBooks(request):
#     book_list = Book.objects.all().only('book_id, book_name')
#     book_list_serializer = BookSerializer(book_list, many=True)
#     return Response(book_list_serializer.data)


@api_view(['GET'])
def getBookAndAuthorById(request, pk):
    try:
        book_and_author_details = Book.objects.get(pk=pk)
        book_and_author_details_serializer = BookSerializer(book_and_author_details)
        return Response(book_and_author_details_serializer.data)

    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getBooksAndAuthors(request):
    books_and_authors_list = Book.objects.all()
    books_and_authors_list_serializer = BookSerializer(
        books_and_authors_list, many=True)
    return Response(books_and_authors_list_serializer.data)


@api_view(['POST'])
def addBook(request):
    add_book_serializer = BookSerializer(data=request.data)
    if add_book_serializer.is_valid():
        add_book_serializer.save()
        return Response(add_book_serializer.data, status=status.HTTP_201_CREATED)
    return Response(add_book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addAuthor(request):
    add_author_serializer = AuthorSerializer(data=request.data)
    if add_author_serializer.is_valid():
        add_author_serializer.save()
        return Response(add_author_serializer.data, status=status.HTTP_201_CREATED)
    return Response(add_author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
