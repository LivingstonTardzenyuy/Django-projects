from django import forms
from .models import *

class Products(forms.ModelForm):

    class Meta:
        model = Items
        fields = "__all__"
