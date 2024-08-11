from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListApiView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title']

    #1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all books\n
        For search book by title add query parameter search\n
        Example: /api/books?search=\<book title\>\n
        \<book title\> can be part of title or full title (case-insentitive)
        '''

        title = request.query_params.get("search")
        if title is not None:
            books = Book.objects.all().filter(title__iregex=rf"{title}")
        else:
            books = Book.objects.all()
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create book
        '''
        data = {
            'title': request.data.get('title')
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete all
    def delete(self, request, *args, **kwargs):
        '''
        Deletes all books
        '''
        Book.objects.all().delete()
        Author.objects.all().delete()
        return Response(
            {"res": "All books deleted!"},
            status=status.HTTP_200_OK
        )


class BookDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, book_id):
        '''
        Helper method to get book by id
        '''
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, book_id, *args, **kwargs):
        '''
        Get book by id
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Book with specified id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, book_id, *args, **kwargs):
        '''
        Update book by id
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Book with specified id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title')
        }
        serializer = BookSerializer(instance = book_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, book_id, *args, **kwargs):
        '''
        Delete book by id
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Book with specified id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res": "Book deleted!"},
            status=status.HTTP_200_OK
        )


class AuthorListApiView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List authors\n
        For search author by name add query parameter search\n
        Example: /api/authors?search=\<author name\>\n
        \<author name\> can be part of name or full name (case-insentitive)
        '''

        name = request.query_params.get("search")
        if name is not None:
            authors = Author.objects.all().filter(name__iregex=rf"{name}")
        else:
            authors = Author.objects.all()

        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create author
        '''
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete all
    def delete(self, request, *args, **kwargs):
        '''
        Delete all authors
        '''
        Author.objects.all().delete()
        return Response(
            {"res": "All authors deleted!"},
            status=status.HTTP_200_OK
        )



class AuthorDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, author_id):
        '''
        Helper method to get author by id
        '''
        try:
            return Author.objects.get(author_id=author_id)
        except Author.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, author_id, *args, **kwargs):
        '''
        Get author by
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Author with specified id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, author_id, *args, **kwargs):
        '''
        Update author by id
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Author with specified id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name')
        }
        serializer = AuthorSerializer(instance = author_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, author_id, *args, **kwargs):
        '''
        Delete author by id
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Author with specified id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        author_instance.delete()
        return Response(
            {"res": "Author deleted!"},
            status=status.HTTP_200_OK
        )
