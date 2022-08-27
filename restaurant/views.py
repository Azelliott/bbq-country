from django.views.generic import TemplateView
from django.views.generic import CreateView
from django import forms
from django.urls import reverse_lazy
from restaurant.models import Customer
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

class MenuPage(TemplateView):
    template_name = "menu.html"

class GalleryPage(TemplateView):
    template_name = "gallery.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class SignUpPage(SuccessMessageMixin, CreateView):
    template_name = "sign-up.html"

    model = Customer
    fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone']
    password = forms.CharField(label='Password*',widget=forms.PasswordInput(attrs={'placeholder': 'alphanumeric password'}))

    
    success_url = reverse_lazy('home')
    success_message = 'User created sucessfully!'

