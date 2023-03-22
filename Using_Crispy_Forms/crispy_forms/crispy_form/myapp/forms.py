from django import forms        
from .models import *


class Registration(forms.ModelForm):
    class Meta:
        model=Employees
        fields='__all__'