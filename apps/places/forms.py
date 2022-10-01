from django import forms
from apps.places.models import Place

class PlaceForm(forms.ModelForm):

    logo = forms.ImageField(
                required=False,
                widget=forms.FileInput(attrs={
                        'class':'form-control'})
    )
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
    phone_number = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={
                            'placeholder': '(+57) Número de teléfono',
                            'class':'form-control'})
    )
    opening_hours = forms.CharField(max_length=50, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Horario de atención - (días / horas)',
                        'class':'form-control'})
    )
    visit_date = forms.DateField(
                required=True,
                widget=forms.DateInput(attrs={
                        'placeholder': 'YYYY-MM-DD',
                        'class':'form-control'})
    )

    class Meta:
        model = Place
        fields = (
            'name', 
            'direction', 
            'phone_number', 
            'opening_hours', 
            'visit_date', 
            'logo', 
            'photo',)
