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
