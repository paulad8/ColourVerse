from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Movement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, related_name='artworks')
    medium = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')

    def __str__(self):
        return self.title
