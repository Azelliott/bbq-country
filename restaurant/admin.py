from django.contrib import admin
from .models import Customer, Review, Reservation
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Reservation)
