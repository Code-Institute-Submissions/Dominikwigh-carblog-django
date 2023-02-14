from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)
# Post page with form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title here!'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your blog text here!'})
            }


# Edit page with form 
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
            }


# Contact page with form

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment!'}),
            }