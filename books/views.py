from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GenreSerializer, BookListSerializer, BookSerializer
from .models import Book, Genre


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        genre = self.get_object()
        books = genre.books.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('genre').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'is_premium', 'publication_year']
    search_fields = ['title', 'author_name', 'description']
    ordering_fields = ['created_at', 'publication_year', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer

    @action(detail=False, methods=['get'])
    def premium(self, request):
        premium_books = self.queryset.filter(is_premium=True)
        serializer = self.get_serializer(premium_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def free(self, request):
        free_books = self.queryset.filter(is_premium=False)
        serializer = self.get_serializer(free_books, many=True)
        return Response(serializer.data)
