from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    birth_year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Year'}), required=False)
    death_year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Year'}), required=False)

    class Meta:
        model = Artist
        fields = ['name', 'region', 'birth_year', 'death_year', 'nationality', 'bio', 'media']