
from django.forms import ModelForm
from django import forms
from .models import Picture

class UploadForm(ModelForm):
    image=forms.ImageField()
    class Meta:
        model = Picture
        fields = ['image',]