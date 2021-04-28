# from django.conf.urls import url
from django.urls import path
from .apis import add_author, get_all_authors, get_author_by_id, update_author_by_id, delete_author_by_id, get_books, add_book, get_book_by_id, update_book_by_id, delete_book_by_id

urlpatterns = [
    path('getAllAuthors/', get_all_authors),
    path('addAuthor/', add_author),
    path('getAuthorById/<int:pk>/', get_author_by_id),
    path('updateAuthorById/<int:pk>/', update_author_by_id),
    path('deleteAuthorById/<int:pk>/', delete_author_by_id),

    path('getAllBooksAndAuthors/', get_books),
    path('addBook/', add_book),
    path('getBookAndAuthorById/<int:pk>/', get_book_by_id),
    path('updateBookById/<int:pk>/', update_book_by_id),
    path('deleteBookById/<int:pk>/', delete_book_by_id),
]
