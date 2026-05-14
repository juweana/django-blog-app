from django.db import models
from django import forms


# Create your models here.
class Course (models.Model):
    title = models. CharField (max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

def __str__(self):
    return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.name


    
    


    