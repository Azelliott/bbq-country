#test booking form
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Test login form
class TestForms(TestCase):
    '''Test cases for the restaurant app'''

    # Test booking form for unauthenticated user, user should be redirected to login page
    def test_booking_form_for_unauthenticated_user(self):
        '''Test that the booking form is rendered'''
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/booking/')
        self.assertTemplateNotUsed(response, 'booking.html')
    
    # Test booking form for authenticated user
    def test_booking_form_for_authenticated_user(self):
        '''Test that the booking form is rendered'''
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword123#'
        )
        self.client.login(username='testuser', password='testpassword123#')
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')
    
    # Test booking form with valid data, user should be redirected to my_reservations page
    # after successful booking
    def test_booking_form_with_valid_data(self):
        '''Test that the booking form is rendered'''
       
       # Log in with valid user
        

        self.client.login(username='testuser', password='testpassword123#')
        response = self.client.post(reverse('booking'), {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test_user@test.com',
            'phone': '+3531234567890',
            'reservation_date': '2023-12-12',
            'reservation_time': '12:00',
            'number_of_people': '2'
        })
        # show page with success message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

        








        

