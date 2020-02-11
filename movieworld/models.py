from django.db import models
# Create your models here.


class Director(models.Model):
    director_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, default="USA")
    birthday = models.TextField()
    photo_url = models.CharField(max_length=256, default='No Image Available')
    bio = models.CharField(max_length=500, default='No information available' )
    def __str__(self):
        return self.director_name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_names')
    name = models.CharField(max_length=100, default='no name')
    genre = models.CharField(max_length=100, default='no genre')
    release_date = models.CharField(max_length=200, null=True)
    synopsis= models.CharField(max_length=500, null=True)
    photo_url = models.CharField(max_length=256, default='No Image Available')
    def __str__(self):
        return self.name



