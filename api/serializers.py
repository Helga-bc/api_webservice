from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(ModelSerializer):
        class Meta:
            model = Book
            fields = ['book_id', 'title']
            


class AuthorSerializer(ModelSerializer):
    books = BookSerializer(many=True, allow_empty=False)
     
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'books']
        
    def create(self, validated_data):
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            author.books.create(**book_data)
        return author
    
    
            
