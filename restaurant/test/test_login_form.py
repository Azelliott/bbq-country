from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm


# Test login form
class TestForms(TestCase):
    '''Test cases for the restaurant app'''

    # Test login form status code
    def test_login_form_status_code(self):
        '''Test that the login form is rendered'''
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    # Test login form with valid user
    def test_login_form_with_valid_user(self):
        '''Test that the login form is rendered'''

        user = User.objects.create_user(
            username='testuser',
            password='testpassword123#'
        )
        form = AuthenticationForm(data={
            'username': 'testuser',
            'password': 'testpassword123#'
        })
        self.assertTrue(form.is_valid())

    # Test login form with invalid user
    def test_login_form_with_invalid_user(self):
        '''Test that the login form is rendered'''

        user = User.objects.create_user(
            username='testuser',
            password='testpassword123#'
        )
        form = AuthenticationForm(data={
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertFalse(form.is_valid())
