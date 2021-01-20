# from django.conf.urls import url
from django.urls import path
from .apis import getAuthors, getBooksAndAuthors

urlpatterns = [
    path('getAuthors/', getAuthors),
    path('getBooksAndAuthors/', getBooksAndAuthors),
]