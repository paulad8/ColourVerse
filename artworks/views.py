from django.shortcuts import render, get_object_or_404
from .models import Artist, Movement, Artwork
import random


def home(request):
    artworks = Artwork.objects.all()
    return render(request, 'gallery/home.html')


def search_by_movement(request, movement):
    # Fetch the movement object based on the provided movement name.
    movement_obj = get_object_or_404(Movement, name=movement)

    # Filter artworks that are associated with the fetched movement.
    artworks = Artwork.objects.filter(movement=movement_obj)

    # Render the 'movement.html' template with the context containing the artworks and movement object.
    return render(request, 'gallery/movement.html', {'artworks': artworks, 'movement': movement_obj})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    artworks = Artwork.objects.filter(artist=artist)
    return render(request, 'gallery/artist_detail.html', {'artist': artist, 'artworks': artworks})

def artists_list(request):
    artists = list(Artist.objects.all())
    random.shuffle(artists)
    return render(request, 'gallery/artists_list.html', {'artists': artists})

def movements_list(request):
    movements = list(Movement.objects.all())
    random.shuffle(movements)
    return render(request, 'gallery/movements_list.html', {'movements' : movements})

def movement(request, movement_name):
    movement = get_object_or_404(Movement, name=movement_name)
    artworks = movement.artworks.all()
    return render(request, 'gallery/movement.html', {
        'movement': movement,
        'artworks': artworks
    })

def random_artworks(request):
    artworks = list(Artwork.objects.all())
    random.shuffle(artworks)
    return render(request, 'gallery/random_artworks.html', {'artworks': artworks[:9]})

def artwork_detail(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    return render(request, 'gallery/artwork_detail.html', {'artwork': artwork})