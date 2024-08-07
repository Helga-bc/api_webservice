from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.generics import ListAPIView


import django_filters 
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated



class BookListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the book items for given requested user
        '''
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Book with given book data
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
        Deletes all books items
        '''
        Book.objects.all().delete()
        return Response(
            {"res": "All Objects deleted!"},
            status=status.HTTP_200_OK
        )


class BookDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, book_id):
        '''
        Helper method to get the object with given book_id
        '''
        try:
            return Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, book_id, *args, **kwargs):
        '''
        Retrieves the Book with given book_id
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, book_id, *args, **kwargs):
        '''
        Updates the book item with given book_id if exists
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"}, 
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
        Deletes the book item with given book_id if exists
        '''
        book_instance = self.get_object(book_id)
        if not book_instance:
            return Response(
                {"res": "Object with book id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




class AuthorListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['name']
    search_fields = ['name']

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the author items
        '''
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Author with given data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete all
    def delete(self, request, *args, **kwargs):
        '''
        Deletes all authors
        '''
        Author.objects.all().delete()
        return Response(
            {"res": "All Objects deleted!"},
            status=status.HTTP_200_OK
        )
        

        
        
    # def get_queryset(self):
    #     """
    #     Optionally returned purchases to a given author,
    #     """
    #     queryset = Author.objects.all()
    #     try:
    #         name = self.request.query_params['search']
    #         if name is not None:
    #             author = queryset.filter(name=name)
    #             serializer = AuthorSerializer(author, many=True)
    #             print(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Exception:
    #         pass
    #         return queryset

        
        
        
        



class AuthorDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, author_id):
        '''
        Helper method to get the object with given author_id
        '''
        try:
            return Author.objects.get(author_id=author_id)
        except Author.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, author_id, *args, **kwargs):
        '''
        Retrieves the Author with given author_id
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # 4. Update
    def put(self, request, author_id, *args, **kwargs):
        '''
        Updates the author item with given author_id if exists
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exist"}, 
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
        Deletes the author item with given author_id if exists
        '''
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author_id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        author_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )





# class AuthorFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Author
#         fields = ['name']


# class AuthorListApiView(APIView):
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_class = AuthorFilter

#     def get(self, request, *args, **kwargs):
#         queryset = Author.objects.all()
#         filterset = self.filterset_class(request.GET, queryset=queryset)
#         if filterset.is_valid():
#             authors = filterset.qs
#             serializer = AuthorSerializer(authors, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)


