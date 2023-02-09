from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Main page with posts #}
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']


# Shows a post when clicked #
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# Add a post 
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'


# Add a category
class AddCategory(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'


# Update the post #
class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


# Delete the post
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')