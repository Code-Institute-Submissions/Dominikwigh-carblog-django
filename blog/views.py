from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

# Main page with posts #}
class Home(ListView):
    model = Post
    template_name = 'home.html'

# Shows a post when clicked #}
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# Add a post #}
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'

# Update the post #
class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
