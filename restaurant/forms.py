from django import forms
from crispy_forms.helper import FormHelper
from .models import Reservation
from .models import Review


class BookingForm(forms.ModelForm):
    """Booking form"""

    class Meta:
        """Meta class for BookingForm"""

        model = Reservation

        first_name = forms.CharField(required=True)

        last_name = forms.CharField()

        email = forms.EmailField()

        phone = forms.CharField()

        reservation_date = forms.DateField()

        reservation_time = forms.TimeField()

        number_of_people = forms.IntegerField()

        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "reservation_date",
            "reservation_time",
            "number_of_people",
        )

        help_texts = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "phone": "Phone",
            "reservation_date": "Reservation Date",
            "reservation_time": "Reservation Time",
            "number_of_people": "Number of People",
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"


class ReviewForm(forms.ModelForm):
    """Review form"""

    class Meta:
        """Meta class for Review form"""

        model = Review
        title = forms.CharField(required=True)
        review = forms.CharField(required=True)
        rating = forms.IntegerField(required=True)
        fields = ("title", "review", "rating")

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
