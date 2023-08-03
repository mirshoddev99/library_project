from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


class BookListAPIView(APIView):
    def get(self, request, *args, **kwarg):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {'status': f'returned {len(books)} books', 'books': serializer.data}
        return Response(data)


class BookCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': "the book was created successfully", 'book': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors})


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book).data
            return Response(serializer)
        except Exception:
            data = {'status': status.HTTP_404_NOT_FOUND, 'msg': 'the book was not found'}
            return Response(data=data)


class BookDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            data = {'status': status.HTTP_204_NO_CONTENT, 'msg': 'the book was deleted'}
            return Response(data=data)
        except Exception:
            data = {'status': status.HTTP_404_NOT_FOUND, 'msg': 'the book was not found'}
            return Response(data=data)


class BookUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(instance=book, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': "the book was updated successfully", 'book': serializer.data})
        except Exception:
            return Response({'error': "Serializer is not valid", 'status': status.HTTP_400_BAD_REQUEST})


# ViewSet
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
