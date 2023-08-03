from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer


class BookListCreateAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailDeleteUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPI(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPI(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
