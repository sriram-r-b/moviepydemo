from django import forms
from .models import Image

class ImageForm(forms.Form):
    image = forms.ImageField(required=True)
