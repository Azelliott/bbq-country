from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

class MenuPage(TemplateView):
    template_name = "menu.html"