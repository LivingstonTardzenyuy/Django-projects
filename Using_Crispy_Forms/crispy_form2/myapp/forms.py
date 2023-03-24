from django import forms        
from .models import *

#validation importation
from django.core.validators import RegexValidator


class Registration(forms.ModelForm):
    
    #validation
    firstname = forms.CharField(
                                label='First name',
                                min_length=5,
                                max_length=50,
                                validators = [RegexValidator(r'^[a-zA-Z0-9]*$',
                                message="Please Only letter are allowed!")],
                                # required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'First-name'})
                                )
    
    lastname = forms.CharField(
                            label='last name',
                            min_length=5,
                            max_length=50,
                            validators = [RegexValidator(r'^[a-zA-Z0-9]*$',
                            message="Please Only letter are allowed!")],
                            # required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'lastname-name'})
                            )
    
    
    email = forms.CharField(
                        label='Email address',
                        min_length=8,
                        max_length=50,
                        validators = [RegexValidator(r'^[a-zA-Z0-9]*$',
                        message="Enter a valid Email!")],
                        # required=False,
                        widget=forms.TextInput(attrs={'placeholder': 'Email address'})
                        )
    
    
    age=forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))
    # age = models.CharField(
        # label='Enter your age',
        # validators=[RegexValidator(r'^[0-9]*$',
        # message="Only numbers is allowed! ")],
        # widget=forms.TextInput(attrs={'placeholder': 'Age'})
    # )
    
    # message=forms.CharField(
                # label='About you',
                # min_length=50,
                # max_length=1000,
                # validators = [RegexValidator(r'^[a-zA-Z0-9]*$',
                # message="Please Only letter are allowed!")],
                # required=False,
                # widget=forms.TextInput(attrs={'placeholder': 'Enter text', 'row':10, 'col': })
                # )    
    class Meta:
        model=Employees
        fields='__all__'
        
        #fields=['firstname', 'lastname', 'email', 'messge', 'created_at', 'age']
        #fields=['firstname', 'lastname', 'email', 'messge', 'created_at', 'age']
