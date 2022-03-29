from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # email=models.EmailField()
    type=models.CharField(max_length=15)

class Post(models.Model):
    author=models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    # blogger=models.CharField(max_length=100)
    image=models.FileField()
    desc=RichTextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.TextField()
    def __str__(self):
        return self.fname


class Service(models.Model):
    name=models.CharField(max_length=100)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    desc=RichTextField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
  

class Purchase(models.Model):
    name=models.CharField(max_length=50)
    foundation=models.CharField(max_length=50)
    email=models.EmailField()
    pdf1=models.FileField(null=True,blank=True)
    
    def __str__(self):
        return self.name