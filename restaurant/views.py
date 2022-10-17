from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
# import missing modules
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Reservation
from .forms import BookingForm

from restaurant.models import Reservation


# Create your views here.

class HomePage(TemplateView):
    ''' Home page view '''
    template_name = "index.html"

class MenuPage(TemplateView):
    ''' Menu page view '''
    template_name = "menu.html"

class GalleryPage(TemplateView):
    ''' Gallery page view '''
    template_name = "gallery.html"

class AboutPage(TemplateView):
    ''' About page view '''
    template_name = "about.html"

class BookingPage(CreateView):
    ''' Booking page view '''
    model = Reservation
    template_name = "booking.html"
    fields = ('first_name', 'last_name', 'email', 'phone', 'reservation_date', 'reservation_time', 'number_of_people')
    success_url='home'
    success_message = "Your booking has been made successfully, we will contact you shortly."

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy(self.success_url)

class MyReservationsPage(TemplateView):
    ''' My reservations page view '''
    template_name = "my_reservations.html"

    # Get reservation date, time and number of people of currently logged in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(email=self.request.user.email)
        return context

# Update reservation view that changes the current reservation and shows success message
def update_reservation(request, pk):
    ''' Update reservation view '''
    reservation = Reservation.objects.get(id=pk)
    form = BookingForm(instance=reservation)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Your reservation has been updated successfully.")
            return redirect('my_reservations')
    context = {'form': form}
    return render(request, 'booking.html', context)

# Delete the reservation from database and shows success message
def delete_reservation(request, pk):
    ''' Delete reservation view '''
    reservation = Reservation.objects.get(id=pk)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Your reservation has been deleted successfully.")
        return redirect('my_reservations')
    context = {'item': reservation}
    return render(request, 'my_reservations.html', context)