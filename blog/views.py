from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Home view 
class Home(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'add_posts.html'
    fields = '__all__'
