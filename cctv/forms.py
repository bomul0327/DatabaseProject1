from django import forms

from .models import File

class DocumentForm(forms.Form):
    docfile = forms.FileField(
    )