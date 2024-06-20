from django.db import models

# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, related_name='artworks')
    medium = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Movement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

