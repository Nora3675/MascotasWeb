from django import forms
from .models import Post

from django.contrib.auth.forms import UserCreationForm, UserChangeForm #*


class BlogForms(forms.ModelForm):
    
    class Meta:
        model=Post
        
        fields='__all__'
        #fields=['imagen']
    
  
