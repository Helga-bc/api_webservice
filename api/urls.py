from django.urls import path, include
from .views import (
    BookListApiView,
    BookDetailApiView,
    AuthorListApiView,
    AuthorDetailApiView
)

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/<uuid:book_id>/', BookDetailApiView.as_view()),
    path('authors/', AuthorListApiView.as_view()),
    path('authors/<uuid:author_id>/', AuthorDetailApiView.as_view())
]