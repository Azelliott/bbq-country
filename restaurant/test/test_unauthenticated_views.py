'''Test cases for the restaurant app'''
from django.test import TestCase
from django.urls import reverse

# Test GET method on unauthenticated views: Index, Menu, Gallery, Reviews
class TestViews(TestCase):
    '''def test_reviews_get(self):'''

    def test_index_get(self):
        '''Test that the index page is rendered'''

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_menu_get(self):
        '''Test that the menu page is rendered'''

        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_gallery_get(self):
        '''Test that the gallery page is rendered'''

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_reviews_get(self):
        '''Test that the reviews page is rendered'''

        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')

    # Test GET method on unauthenticated views: Booking, My Reservations, Add Review

    def test_booking_get(self):
        '''Test that the booking page is rendered'''

        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/booking/')
        self.assertTemplateNotUsed(response, 'booking.html')

    def test_my_reservations_get(self):
        '''Test that the my reservations page is rendered'''

        response = self.client.get(reverse('my_reservations'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/my_reservations/')
        self.assertTemplateNotUsed(response, 'my_reservations.html')

    def test_add_review_get(self):
        '''Test that the add review page is rendered'''

        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/add_review/')
        self.assertTemplateNotUsed(response, 'add_review.html')
        