from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Reservation

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'email', 'phone', 'reservation_date', 'reservation_time', 'number_of_people')
        widgets = {
            'reservation_date': DatePickerInput(format='%Y-%m-%d'),
        }
