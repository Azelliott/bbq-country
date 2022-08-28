from django.views.generic import TemplateView
from django.views.generic import CreateView
from django import forms
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from restaurant.models import Reservation


# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

class MenuPage(TemplateView):
    template_name = "menu.html"

class GalleryPage(TemplateView):
    template_name = "gallery.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class BookingPage(CreateView):
    model = Reservation
    template_name = "booking.html"
    fields = ('first_name', 'last_name', 'email', 'phone', 'reservation_date', 'reservation_time', 'number_of_people')
    success_url='home'

