from django.db import models
from enum import Enum

from django.db.models.base import Model

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images',null=True,blank=True)
    video = models.FileField(upload_to='media/videos',null=True,blank=True)
    is_photo = models.BooleanField(default=True)
    class Meta:
        ordering = ['-created_at']

    def __self__(self):
        return self.title


class BlogDetail(models.Model):
    Blog = models.OneToOneField(Blog,on_delete=models.CASCADE,related_name='detail')
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content3_title = models.CharField(max_length=256)
    content4 = models.TextField()
    content4_title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media/images')
    video = models.FileField(upload_to='media/video')

    def __str__(self):
        return str(self.id)




class Project(models.Model):
    class Category(Enum):
        WEBAPPD='webappd'
        BRANDMARKET='brandmarket'
        CONTENTDESIGN='contentdesign'
        DED='ded'
        OTHER='other'

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]
    class Type(Enum):
        TYPE1=1
        TYPE2=2
        TYPE3=3        

        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]

    class Meta:
        ordering = ['-created_at']

    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='media/images',blank=True,null=True)
    video = models.FileField(upload_to='media/videos',blank=True,null=True)
    category = models.CharField(max_length=256,choices=Category.choices(),default=Category.OTHER)
    is_photo = models.BooleanField(default=True)
    type = models.IntegerField(choices=Type.choices(),default=1)
    def __self__(self):
        return self.title


class ProjectMedia(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='media_content')
    image = models.ImageField(upload_to='media/images',null=True,blank=True)
    video = models.FileField(upload_to='media/videos',null=True,blank=True)
    is_photo = models.BooleanField(default=True)

class ProjectContent(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='text_content')
    text = models.TextField(blank=True,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.email
    