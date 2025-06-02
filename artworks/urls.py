from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#from django.conf.urls import handler404, handler500
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('movement/<str:movement>/', views.search_by_movement, name='search_by_movement'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('artists/', views.artists_list, name='artists_list'),
    path('movements/', views.movements_list, name='movements_list'),
    path('random_artworks/', views.random_artworks, name='random_artworks'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    #path('movement/<str:movement_name>/', views.movement, name='movement'),
    path('media/<str:media>/', views.artworks_by_media, name='artworks_by_media'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'artworks.views.custom_404'
handler500 = 'artworks.views.custom_500'