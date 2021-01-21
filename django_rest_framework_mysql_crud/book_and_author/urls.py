# from django.conf.urls import url
from django.urls import path
from .apis import getAuthors, getBooksAndAuthors, addAuthor, addBook, getAuthorById, getBookAndAuthorById

urlpatterns = [
    path('getAuthors/', getAuthors),
    path('getAuthorById/<int:pk>/', getAuthorById),
    # path('getBooks/', getBooks),
    path('getBooksAndAuthors/', getBooksAndAuthors),
    path('getBookAndAuthorById/<int:pk>/', getBookAndAuthorById),
    path('addAuthor/', addAuthor),
    path('addBook/', addBook),
]