from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    genre_display = serializers.CharField(
        source='get_genre_display',
        read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'isbn',
            'genre',
            'genre_display',
            'published_date',
            'publisher',
            'page_count',
            'language',
            'description',
            'cover_image_url',
            'price',
            'in_stock',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'isbn': {'required': True},
            'price': {'min_value': 0},
            'page_count': {'min_value': 1},
            'in_stock': {'min_value': 0},
        }