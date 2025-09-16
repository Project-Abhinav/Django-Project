from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog (models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='photos/',blank=True ,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return f'{self.user.username}-{self.text[:10]}'
    
    