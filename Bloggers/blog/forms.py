from django import forms
from .models import  Blog 

class Blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("text","image")
