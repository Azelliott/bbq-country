from django.contrib import admin
from .models import Customer, Review, Reservation

# Register your models here.
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Reservation)