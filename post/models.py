from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    view = models.IntegerField(default=0, editable=False)
    categories = models.ManyToManyField(Category)
    created = models.DateField(auto_now_add=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
