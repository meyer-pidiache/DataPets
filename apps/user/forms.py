from django import forms
from apps.main.models import Review

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