from django import forms
from .models import Lead


class FreeProductForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'email']
