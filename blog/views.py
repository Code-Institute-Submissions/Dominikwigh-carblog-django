from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Home view 
class Home(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
