from django import forms
from apps.places.models import Place

class PlaceForm(forms.ModelForm):

    photo = forms.ImageField(
                required=False,
                widget=forms.FileInput(attrs={
                        'class':'form-control'})
    )
    name = forms.CharField(max_length=50, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Nombre del lugar',
                        'class':'form-control'})
    )
    direction = forms.CharField(max_length=50, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Dirección',
                        'class':'form-control'})
    )
    visit_date = forms.DateField(
                required=True,
                # TODO MM/DD/YYYY
                widget=forms.DateInput(attrs={
                        'placeholder': 'YYYY-MM-DD',
                        'class':'form-control'})
    )

    class Meta:
        model = Place
        fields = (
            'name', 
            'direction', 
            'visit_date', 
            'photo',)
