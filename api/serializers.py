from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(ModelSerializer):
    
        class Meta:
            model = Book
            fields = ['book_id', 'title']
            


class AuthorSerializer(ModelSerializer):
    books = BookSerializer(many=True)
     
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'books']
        
    def create(self, validated_data):
        books = validated_data.pop('books')
        
        author = Author.objects.create(**validated_data)
        author.books.add(*books)
        
        print("____________________________")
        return author
            
