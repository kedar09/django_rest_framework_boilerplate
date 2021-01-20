from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from django.http import Http404
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

@api_view(['GET'])
def getAuthors(request):
    author_list = Author.objects.all()
    author_list_serializer = AuthorSerializer(author_list,many = True)
    return JsonResponse({"message": "success", "status": 200, "response": author_list_serializer.data})
                
@api_view(['GET'])
def getBooksAndAuthors(request):
    book_list = Book.objects.prefetch_related('author_id')
    book_list_serializer = BookSerializer(book_list,many = True)
    return JsonResponse({"message": "success", "status": 200, "response": book_list_serializer.data})

