from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUp_form(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model= User
        fields=['username', 'email', 'password1', 'password2']
        
        
        #getting ride of the help text
        
    def __init__(self, *args, **kwargs):
        super(SignUp_form, self).__init__(*args, **kwargs)      #overwirte
        
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
            
class Profileprofileupdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']


class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
        super(UserProfileUpdate, self).__init__(*args, **kwargs)
    
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

    



