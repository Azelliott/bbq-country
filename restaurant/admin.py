from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review, Reservation


@admin.register(Review)
class AdminReview(SummernoteModelAdmin):
    ''' Admin class for Review model '''

    def username(self, obj):
        ''' Return username of user who wrote the review '''
        return obj.user.username

    summernote_fields = 'review'
    search_fields = ('username', 'review', 'reviewed_on')
    list_display = ('username', 'review', 'reviewed_on')
    list_filter = ('user__username', 'review', 'reviewed_on')


@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    ''' Admin class for Reservation model '''

    def username(self, obj):
        ''' Return username of user who made the reservation '''
        return obj.user.username

    def first_name(self, obj):
        ''' Get First Name field '''
        return obj.user.first_name

    def last_name(self, obj):
        ''' Get Last Name field '''
        return obj.user.last_name

    def email(self, obj):
        ''' Get Email field '''
        return obj.user.email

    def phone(self, obj):
        ''' Get Phone field '''
        return obj.user.phone

    def reservation_date(self, obj):
        ''' Get reservation Date field '''
        return obj.reservation_date

    def reservation_time(self, obj):
        ''' Get reservation Time field '''
        return obj.reservation_time

    def number_of_people(self, obj):
        ''' Get reservation Number of People field '''
        return obj.number_of_people

    search_fields = ('first_name', 'last_name', 'email', 'phone',
                     'reservation_date', 'number_of_people')

    list_display = ('username', 'first_name', 'last_name', 'email', 'phone',
                    'reservation_date', 'number_of_people')

    list_filter = ('reservation_date', 'number_of_people')
