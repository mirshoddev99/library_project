from django.urls import path, include
from books.views import BookListAPIView, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, BookCreateAPIView, \
    BookViewSet
from rest_framework.routers import SimpleRouter

# Router for working with ViewSets
router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/<int:pk>/detail/', BookDetailAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
]

urlpatterns += router.urls
