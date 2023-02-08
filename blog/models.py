from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, default='blogpost')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='car')

    def __str__(self):
        return self.title + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    

