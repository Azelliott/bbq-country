from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Reservation, Review
from .forms import BookingForm




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


@method_decorator(login_required, name='dispatch')
class BookingPage(CreateView):
    ''' Booking page view '''
    model = Reservation
    template_name = "booking.html"
    fields = ('first_name', 'last_name', 'email', 'phone', 'reservation_date', 'reservation_time', 'number_of_people')
    success_url='my_reservations'
    success_message = "Your booking has been made successfully, we will contact you shortly."
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy(self.success_url)


@method_decorator(login_required, name='dispatch')
class MyReservationsPage(TemplateView):
    ''' Show reservations page view for authenticated user'''
    template_name = "my_reservations.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(user=self.request.user)
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

# Delete reservation data by id and show success message
def delete_reservation(request, pk):
    ''' Delete reservation view '''
    reservation = Reservation.objects.get(id=pk)
    if request.method == "GET":
        reservation.delete()
        messages.success(request, "Your reservation has been deleted successfully.")
        return redirect('my_reservations')
    context = {'item': reservation}
    return render(request, 'delete_reservation.html', context)

class ReviewsPage(TemplateView):
    ''' Reviews page view shows paginated results sorted by latest reviewed_on '''
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all().order_by('-reviewed_on')
        page = self.request.GET.get('page', 1)
        paginator = Paginator(reviews, 4)
        try:
            reviews = paginator.page(page)
        except PageNotAnInteger:
            reviews = paginator.page(1)
        except EmptyPage:
            reviews = paginator.page(paginator.num_pages)
        context['reviews'] = reviews
        return context

    


class AddReviewPage(CreateView):
    ''' Add review page view '''
    model = Review
    template_name = "add_review.html"
    fields = ('title', 'review', 'rating')
    success_url='reviews'
    success_message = "Your review has been added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy(self.success_url)
