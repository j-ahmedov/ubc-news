from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import News


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'media', 'category']
