from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile



class User_signup(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(User_signup, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
class Profile_page(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'mobile_number']