from django import forms
from django.contrib.auth.forms import UserCreationForm
from news.models import User, News


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'username', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=65),
    last_name = forms.CharField(max_length=65),
    username = forms.CharField(max_length=65),
    avatar = forms.ImageField()
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar', 'password']


class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'media', 'category']
