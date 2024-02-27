from django import forms
from datetime import datetime


class UserComment(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'user@mail.ru'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Введите комментарий'}))
    created_date = forms.DateTimeField(initial=datetime.utcnow)





