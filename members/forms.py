from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


# Edit profile form
class EditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'}))
    first_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    username = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_login = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'last_login', 'is_staff', 'is_active', 'is_superuser')


# Register form
class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'}))
    first_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# Profile page creation
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'facebook', 'instagram', 'linkedin')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),

        }
