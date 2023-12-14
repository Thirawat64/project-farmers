from django import forms
from .models import *

class Search1(forms.Form):
    search = forms.CharField(label='Search')
