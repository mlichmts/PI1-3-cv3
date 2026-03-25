from django import forms
from .models import Kruzok

class KruzokForm(forms.ModelForm):
    class Meta:
        model = Kruzok
        fields = ['nazov', 'den', 'miestnost', 'veduci']