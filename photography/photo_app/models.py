from django.db import models
from django import forms

# Create your models here.
class Pages(models.Model):
    Name= models.CharField(max_length=264,unique=True)
    content = models.TextField(max_length=20000)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Post(models.Model):
    name=models.CharField(max_length=264,unique=True)
    content = models.TextField(max_length=20000,null=True)
    classname=models.CharField(max_length=264,null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
