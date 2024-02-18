from django import forms
from .models import Product

class ImageForm(forms.Form):
    image = forms.ImageField()


    class Meta:
        model = Product
        fields = ['name', 'picture']