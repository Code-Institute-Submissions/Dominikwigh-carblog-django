from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from .forms import SignupForm, ProfilePageForm
from django.views.generic import DetailView, CreateView
from blog.models import Profile
from django.contrib.messages.views import SuccessMessageMixin


# Registration
class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "You have registered and logged in"


# Edit profile
class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    success_message = "You have edited your profile"

    def get_object(self):
        return self.request.user


# Profile page
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self,).get_context_data(
            *args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['Profile'] = profile
        return context


# Edit profile page
class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'facebook', 'instagram', 'linkedin']
    success_url = reverse_lazy('home')
    success_message = "You have edited your profile"


# Create a profile page
class CreateProfilePageView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user.html'
    success_message = "You have created your profile"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
