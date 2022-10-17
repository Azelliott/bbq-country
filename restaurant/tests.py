from django.test import TestCase
from .models import Reservation

# Create your tests here.

# Write all tests
class TestViews(TestCase):
    '''Class to test views'''
    def test_get_home_page(self):
        '''Test to get home page'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_menu_page(self):
        '''Test to get menu page'''
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_get_gallery_page(self):
        '''Test to get gallery page'''
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_get_about_page(self):
        '''Test to get about page'''
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_booking_page(self):
        '''Test to get booking page'''
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_post_booking_page(self):
        '''Test to post booking page'''
        response = self.client.post('/booking/', {
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@test.com',
            'phone': '1234567890',
            'reservation_date': '2020-01-01',
            'reservation_time': '12:00',
            'number_of_people': '1',
        })
