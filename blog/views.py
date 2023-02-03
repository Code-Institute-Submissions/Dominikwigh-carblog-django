from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Home view 
class Home(ListView):
    model = Post
    template_name = 'home.html'
