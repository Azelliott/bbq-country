from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Customer, Review, Reservation


@admin.register(Review)
class AdminReview(SummernoteModelAdmin):
    ''' Admin class for Review model '''

    def username(self, obj):
        ''' Return username of customer who wrote the review '''
        return obj.customer.username


    summernote_fields = 'review'
    search_fields = ('username', 'review', 'reviewed_on')
    list_display = ('username', 'review', 'reviewed_on')
    list_filter = ('customer__username', 'review', 'reviewed_on')


@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    ''' Admin class for Reservation model '''

    def username(self, obj):
        ''' Get Customer Username field '''
        return obj.customer.username

    def first_name(self, obj):
        ''' Get Customer First Name field '''
        return obj.customer.first_name

    def last_name(self, obj):
        ''' Get Customer Last Name field '''
        return obj.customer.last_name

    def email(self, obj):
        ''' Get Customer Email field '''
        return obj.customer.email

    def phone(self, obj):
        ''' Get Customer Phone field '''
        return obj.customer.phone

    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone'
    ,'reservation_date_time', 'number_of_people', 'reservation_confirmed')

    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'reservation_date_time', 'number_of_people', 'reservation_confirmed')

    list_filter = ('customer__first_name', 'customer__last_name', 'customer__username'
    ,'customer__email', 'customer__phone', 'reservation_date_time'
    ,'number_of_people', 'reservation_confirmed')


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    ''' Admin class for Customer model '''

    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'has_reservation')
    list_display = ('first_name', 'last_name', 'username', 'email', 'phone', 'has_reservation')
    list_filter = ('first_name', 'last_name', 'username', 'email', 'phone', 'has_reservation')
