from django.db import models
from django.core.validators import MinLengthValidator

class Book(models.Model):
    class Genre(models.TextChoices):
        FICTION = 'FIC', 'Fiction'
        NON_FICTION = 'NON', 'Non-Fiction'
        SCIENCE = 'SCI', 'Science'
        HISTORY = 'HIS', 'History'
        BIOGRAPHY = 'BIO', 'Biography'
        FANTASY = 'FAN', 'Fantasy'
        ROMANCE = 'ROM', 'Romance'
        THRILLER = 'THR', 'Thriller'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(10)],
        unique=True
    )
    genre = models.CharField(
        max_length=3,
        choices=Genre.choices,
        default=Genre.FICTION
    )
    published_date = models.DateField()
    publisher = models.CharField(max_length=100)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    cover_image_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['genre']),
            models.Index(fields=['isbn']),
        ]