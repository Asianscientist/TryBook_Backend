from rest_framework import serializers
from .models import Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(source='books.count', read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'books_count']


class BookSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_name', 'description', 'genre', 'genre_name',
            'publication_year', 'file_url', 'cover_url', 'is_premium', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value < 1000 or value > current_year:
            raise serializers.ValidationError(
                f"Publication year must be between 1000 and {current_year}"
            )
        return value


class BookListSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author_name', 'genre_name', 
            'publication_year', 'cover_url', 'is_premium'
        ]
