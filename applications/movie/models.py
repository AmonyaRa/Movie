from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_movies')
    viewer = models.ManyToManyField(User, through='Relation', related_name='movies')
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Relation(models.Model):
    RATING_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return f'{self.owner.username} - {self.movie} - {self.rating}'


class Like(models.Model):
    LIKE_CHOICES = (
        ('👍', 'like'),
        ('👎', 'Unlike')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.CharField(max_length=20, choices=LIKE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.owner.username} - {self.movie} - {self.like}'
