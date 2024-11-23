from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Artist, Movement, Artwork, Medium
from .forms import ArtistForm

class ArtworkInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Artwork
    fields = ('title', 'description', 'medium')  # specify fields to display
    extra = 0  # Prevents extra empty fields from showing up

# Customising the admin interface for the Artist model
class ArtistAdmin(admin.ModelAdmin):
    form = ArtistForm
    inlines = [ArtworkInline]
    list_display = ('name', 'birth_year', 'death_year', 'nationality', 'bio', 'movement', 'display_media')
    search_fields = ('name', 'media')
    list_filter = ['name']
    fields = ['name', 'birth_year', 'death_year', 'nationality', 'media', 'portrait', 'bio', 'movement']

    def display_media(self, obj):
        return ", ".join([medium.name for medium in obj.sample_artwork.medium.all()]) if obj.sample_artwork else 'N/A'

    display_media.short_description = 'Media'

# Customising the admin interface for the Movement model
class MovementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'artworks_list')
    search_fields = ('name',)
    list_filter = ('name',)

    def artworks_list(self, obj):
        return ", ".join([artwork.title for artwork in obj.artworks.all()])

    artworks_list.short_description = "Artworks"

# Customising the admin interface for the Artwork model
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'movement', 'display_medium', 'created_date')
    search_fields = ('title', 'artist__name', 'movement__name', 'medium__name')
    list_filter = ('movement', ('medium', RelatedOnlyFieldListFilter), 'artist')
    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'movement', 'medium', 'description', 'image')
        }),
        ('Additional Info', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )

    def display_medium(self, obj):
        return obj.medium.name if obj.medium else "No Medium"
    display_medium.short_description = 'Medium'

    display_medium.short_description = 'Media'
    readonly_fields = ('created_at', 'updated_at')  # Ensure these fields exist in the Artwork model

class MediumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering the admin classes with the associated models
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Medium, MediumAdmin)


