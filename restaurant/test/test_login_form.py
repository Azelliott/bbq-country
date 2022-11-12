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

    # Test login and logout
    def test_login_and_logout(self):
        '''Test that the login and logout forms are rendered'''
        User.objects.create_user(
            username='testuser',
            password='testpassword123#',
        )
        # Login
        response = self.client.post(reverse('account_login'), {
            'username': 'testuser',
            'password': 'testpassword123#',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, 'testuser')
        self.assertTemplateNotUsed(response, 'account/login.html')
        # Logout
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'account/logout.html')




    # Test login form - empty username - invalid
    def test_login_form_empty_username(self):
        '''Test that the login form is empty username'''
        User.objects.create_user(
            username='testuser',
            password='testpassword123#',
        )
        form = AuthenticationForm(data={
            'username': '',
            'password': 'testpassword123#',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    # Test login form - empty password - invalid
    def test_login_form_empty_password(self):
        '''Test that the login form is empty password'''
        User.objects.create_user(
            username='testuser',
            password='testpassword123#',
        )
        form = AuthenticationForm(data={
            'username': 'testuser',
            'password': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])

    # Test login form - invalid username - invalid
    def test_login_form_invalid_username(self):
        '''Test that the login form is invalid username'''
        User.objects.create_user(
            username='testuser',
            password='testpassword123#',
        )
        form = AuthenticationForm(data={
            'username': 'testuser1',
            'password': 'testpassword123#',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.' , form.non_field_errors())

    # Test login form - invalid password - invalid
    def test_login_form_invalid_password(self):
        '''Test that the login form is invalid password'''
        User.objects.create_user(
            username='testuser',
            password='testpassword123#',
        )
        form = AuthenticationForm(data={
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.' , form.non_field_errors())

    # Test log out form status code
    def test_logout(self):
        '''Test that the logout form is rendered'''
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'account/logout.html')