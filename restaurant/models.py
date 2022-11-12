from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """Review model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(
        default=5, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    reviewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review)

    class Meta:
        """Meta class for Review model"""

        ordering = ["reviewed_on"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class Reservation(models.Model):
    """Reservation model"""

    # authenticated User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_people = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
