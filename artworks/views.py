from django.shortcuts import render, get_object_or_404
from .models import Artist, Movement, Artwork

def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'gallery/home.html', {'artworks': artworks})

def search_by_movement(request, movement):
    movement_obj = get_object_or_404(Movement, name=movement)
    artworks = Artwork.objects.filter(movement=movement_obj)
    return render(request, 'gallery/movement.html', {'artworks':artworks, 'movement': movement_obj})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    artworks = Artwork.objects.filter(artist=artist)
    return render(request, 'gallery/artist_detail.html', {'artist': artist, 'artworks': artworks})

