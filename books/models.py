from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='books')
    publication_year = models.IntegerField()
    file_url = models.URLField(max_length=500)
    cover_url = models.URLField(max_length=500)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['genre', '-created_at']),
            models.Index(fields=['is_premium']),
        ]

    def __str__(self):
        return f"{self.title} by {self.author_name}"
