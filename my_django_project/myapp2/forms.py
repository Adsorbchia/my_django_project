from django import forms
from .models import Product


class ImageForm(forms.ModelForm):
    # picture = forms.ImageField()

    class Meta:
        model = Product
        fields = ('product_name', 'picture')

