from django.db import models
# Create your models here.


class Director(models.Model):
    director_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birthday = models.TextField()
    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='name')
    name = models.CharField(max_length=100, default='no name')
    genre = models.CharField(max_length=100, default='no genre')
    release_date = models.CharField(max_length=200, null=True)
    director_name= models.CharField(max_length=200, null=True)
    stars= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name



