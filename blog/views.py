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

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self,).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def AddCategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat': cat.title(), 'category_posts':category_posts})


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