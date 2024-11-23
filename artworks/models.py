from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=100, default='Unknown') # Provide a default value
    bio = models.TextField()

    portrait = models.ImageField(upload_to='artist_portraits/', null=True, blank=True)
    sample_artwork = models.ForeignKey('Artwork', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='sampled_artworks')
    movement = models.ForeignKey('Movement', on_delete=models.SET_NULL, null=True, blank=True)
    media = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.add_media_entries()

    def add_media_entries(self):
        if self.media:
            media_list = [item.strip() for item in self.media.split(',')]
            for media_name in media_list:
                medium_obj, created = Medium.objects.get_or_create(name=media_name)
                artworks = self.sample_artwork
                if artworks:
                    artworks.medium.add(medium_obj)

    def __str__(self):
        return self.name

class Movement(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='movement_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, related_name='artworks')
    medium = models.ForeignKey('Medium', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now) # Provide a default value
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure these fields are present
    updated_at = models.DateTimeField(auto_now=True)  # Ensure these fields are present
    image = models.ImageField(upload_to='artworks_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Medium(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name