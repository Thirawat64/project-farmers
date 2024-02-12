from django.forms import ModelForm
from django import forms
from .models import *

class Search1(forms.Form):
    search = forms.CharField(label='Search')


class UploadForm(ModelForm):
    product_name = forms.TextInput()
    product_price = forms.IntegerField()
    phon_number = forms.NumberInput()
    product_detail = forms.TextInput()
    product_size = forms.TextInput()
    product_statustype = forms.TextInput()
    product_location = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = AllProduct
        fields = ['product_name', 'product_price', 'phon_number', 'product_detail', 'product_size', 'product_statustype', 'product_location', 'image']


