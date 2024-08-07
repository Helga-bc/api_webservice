from rest_framework.serializers import ModelSerializer
from .models import Book, Author


class BookSerializer(ModelSerializer):
        class Meta:
            model = Book
            fields = ['book_id', 'title']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'books']
   