from django import forms
from apps.places.models import Place

class PlaceForm(forms.ModelForm):

    place_logo = forms.ImageField(
                required=False,
                widget=forms.FileInput(attrs={
                        'class':'form-control'})
    )
    place_photo = forms.ImageField(
                widget=forms.FileInput(attrs={
                        'class':'form-control'})
    )
    place_name = forms.CharField(max_length=20, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Nombre del lugar',
                        'class':'form-control'})
    )
    place_direction = forms.CharField(max_length=50, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Dirección',
                        'class':'form-control'})
    )
    place_phone_number = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={
                            'placeholder': '(+57) Número de teléfono',
                            'class':'form-control'})
    )
    place_opening_hours = forms.CharField(max_length=50, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Horario de atención - (días / horas)',
                        'class':'form-control'})
    )
    place_visit_date = forms.DateField(
                required=True,
                widget=forms.DateInput(attrs={
                        'placeholder': 'YYYY-MM-DD',
                        'class':'form-control'})
    )

    class Meta:
        model = Place
        fields = (
            'place_name', 
            'place_direction', 
            'place_phone_number', 
            'place_opening_hours', 
            'place_visit_date', 
            'place_logo', 
            'place_photo',)
