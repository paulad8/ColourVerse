from django.contrib import admin
from .models import Artist, Movement, Artwork
from .forms import ArtistForm

# Customising the admin interface for the Artist model
class ArtistAdmin(admin.ModelAdmin):
    form = ArtistForm
    list_display = ('name', 'birth_year', 'death_year', 'nationality')
    search_fields = ('name', 'media')
    list_filter = ['name']
    fields = ['name', 'birth_year', 'death_year', 'nationality', 'media', 'portrait']

# Customising the admin interface for the Movement model
class MovementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

# Customising the admin interface for the Artwork model
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'movement', 'medium', 'created_date')
    search_fields = ('title', 'artist__name', 'movement__name', 'medium')
    list_filter = ('movement', 'medium', 'artist')
    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'movement', 'medium', 'description', 'image')
        }),
        ('Additional Info', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # Ensure these fields exist in the Artwork model

# Registering the admin classes with the associated models
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Artwork, ArtworkAdmin)


