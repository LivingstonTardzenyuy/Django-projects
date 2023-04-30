from django import forms
from .models import *

class Input(forms.ModelForm):
    class Meta:
        model=Reservation
        fields='__all__'
   
   
class Admin_site(forms.ModelForm): 
    class Meta:
        model=AdminLogin
        fields='__all__'
        
        
class Manager_site(forms.ModelForm):
    class Meta:
        model=Manager
        fields='__all__'
        
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'