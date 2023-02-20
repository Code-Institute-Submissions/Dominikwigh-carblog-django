from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, ContactForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


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


# Add category
def AddCategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {
        'cat': cat.title(), 'category_posts': category_posts})


# Shows a post when clicked #
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self,).get_context_data(
            *args, **kwargs)
        context['cat_menu'] = cat_menu
        get_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_likes.total_likes()
        liked = False
        if get_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


# Add a post
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self,).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


# Add a category
class AddCategory(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self,).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


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


# Contact form
def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Blog Inquiry'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'dominik-00@live.se', [
                    'dominik-00@live.se'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, "Message sent.")
            return redirect('contact')
            messages.error(request, "Error. Message not sent.")
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# Like a post
# taken from codemy.com
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


# Add comment
class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
