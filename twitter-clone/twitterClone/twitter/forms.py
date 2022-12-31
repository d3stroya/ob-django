from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'textarea',
        'class': 'form-control',
        'placeholder': '¿Qué está pasando?'
    }))

    class Meta:
        model = Post
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
