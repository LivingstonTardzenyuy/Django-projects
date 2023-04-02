from django import forms

from .models import *

class PostFormModel(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title', 'content']
        
        
class EditPost(forms.ModelForm):
    class Meta:
        model = PostModel
        fields =['title', 'content']
        
class CommentsForm(forms.ModelForm):
    content= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Comment here......'}))
    class Meta:
        model = Comment
        fields = ('content',)