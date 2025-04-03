from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend #type: ignore
from django.db.models import Count  # Add this import
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'author', 'publisher', 'language']
    search_fields = ['title', 'author', 'isbn', 'description']
    ordering_fields = ['title', 'author', 'price', 'published_date', 'created_at']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        queryset = self.get_queryset().filter(in_stock__gt=0)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_genre(self, request):
        genre_stats = (
            Book.objects.values('genre')
            .annotate(count=Count('id'))  # Corrected this line
            .order_by('-count')
        )
        return Response(genre_stats)