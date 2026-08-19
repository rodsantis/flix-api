from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='review')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Rating must be form 0 to 5 stars'),
            MaxValueValidator(5, 'Rating must be from 0 to 5 stars'),
        ]
    )
    comment = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.movie