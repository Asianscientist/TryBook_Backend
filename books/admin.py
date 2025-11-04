from django.contrib import admin
from .models import Genre, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'books_count']
    search_fields = ['name']

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = 'Number of Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_name', 'genre', 'publication_year', 'is_premium', 'created_at']
    list_filter = ['is_premium', 'genre', 'publication_year']
    search_fields = ['title', 'author_name', 'description']
    list_select_related = ['genre']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']

