from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Customer(models.Model):
    ''' Customer model '''
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    phone = models.IntegerField(blank=False)
    registered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    has_reservation = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        ''' Meta class for Customer model '''
        ordering = ['username']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Review(models.Model):
    ''' Review model '''
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = Customer.username
    review = models.TextField(max_length=500)
    reviewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review)

    class Meta:
        ''' Meta class for Review model '''
        ordering = ['reviewed_on']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Reservation(models.Model):
    ''' Reservation model '''
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = Customer.first_name
    last_name = Customer.last_name
    username = Customer.username
    email = Customer.email
    phone = Customer.phone
    reservation_date_time = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField()
    reservation_confirmed = models.BooleanField(default=False)

    def __str__(self):
        ''' String representation of Reservation model '''
        return str(self.reservation_date_time)

    class Meta:
        ''' Meta class for Reservation model '''
        ordering = ['reservation_date_time']
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'