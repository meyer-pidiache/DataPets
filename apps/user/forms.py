from django import forms
from django.contrib.auth.models import User
from apps.main.models import Review
from apps.user.models import Profile


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(
                    max_length=200, required=True,
                    widget=forms.Textarea(attrs={
                        'placeholder': 'Deja aquí tu comentario...',
                        'class':'form-control',
                        'rows':'4'}))

    class Meta:
        model = Review
        fields = ('review_text',)


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
                max_length=10, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Nombre de usuario',
                        'class':'form-control'})
    )
    first_name = forms.CharField(
                max_length=20, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Nombres',
                        'class':'form-control'})
    )
    last_name = forms.CharField(
                max_length=20, required=True,
                widget=forms.TextInput(attrs={
                        'placeholder': 'Apellidos',
                        'class':'form-control'})
    )
    password1 = forms.CharField(
                max_length=20, required=True,
                widget=forms.PasswordInput(attrs={
                        'placeholder': 'Contraseña',
                        'class':'form-control'})
    )
    password2 = forms.CharField(
                max_length=20, required=True,
                widget=forms.PasswordInput(attrs={
                        'placeholder': 'Confirma contraseña',
                        'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(
                        required=False,
                        widget=forms.FileInput(attrs={
                            'class':'form-control'})
    )
    phone_number = forms.CharField(
                    required=True,
                    widget=forms.TextInput(attrs={
                            'placeholder': '(+57) Número de teléfono',
                            'class':'form-control'})
    )

    class Meta:
        model = Profile
        fields = ('profile_picture', 'gender', 'phone_number')