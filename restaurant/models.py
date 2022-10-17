from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from tomlkit import datetime 




class Review(models.Model):
    ''' Review model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = User.username
    review = models.TextField(max_length=500 ,blank=False)
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
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField(blank=True)
    reservation_date = models.DateField(blank=True)
    reservation_time = models.TimeField(blank=True)
    number_of_people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

