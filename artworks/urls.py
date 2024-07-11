from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movement/<str:movement>/', views.search_by_movement, name='search_by_movement'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('artists/', views.artists_list, name='artists_list'),
    path('movements/', views.movements_list, name='movements_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)