from django import forms
from .models import  Blog 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("title","text","image")


class User_registration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




