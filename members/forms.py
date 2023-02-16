from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms 

# Edit profile form
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=120, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=120, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_superuser = forms.CharField(max_length=120, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_staff', 'is_active', 'is_superuser')
