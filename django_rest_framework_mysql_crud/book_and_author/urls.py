# from django.conf.urls import url
from django.urls import path
from .apis import add_get_authors, get_update_delete_author_by_id, add_get_books, get_add_update_book_by_id

urlpatterns = [
    path('getAuthors/', add_get_authors),
    path('addAuthor/', add_get_authors),
    path('getAuthorById/<int:pk>/', get_update_delete_author_by_id),
    path('updateAuthor/<int:pk>/', get_update_delete_author_by_id),
    path('deleteAuthor/<int:pk>/', get_update_delete_author_by_id),
    
    # path('getBooks/', add_get_books),
    path('getBooksAndAuthors/', add_get_books),
    path('addBook/', add_get_books),
    path('getBookAndAuthorById/<int:pk>/', get_add_update_book_by_id),
    path('updateBook/<int:pk>/', get_add_update_book_by_id),
    path('deleteBook/<int:pk>/', get_add_update_book_by_id),
]