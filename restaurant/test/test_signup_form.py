from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


# Test signup form
class TestForms(TestCase):
    '''Test cases for the restaurant app'''

    # Test signup form status code
    def test_signup_form_status_code(self):
        '''Test that the signup form is rendered'''
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    # Test signup form create user - valid
    def test_signup_form_create_user(self):
        '''Test that the signup form creates a user'''
        form = UserCreationForm({
            'username': 'testuser',
            'email': 'test_user@test.com',
            'password1': 'testpassword123#',
            'password2': 'testpassword123#',
        })
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    # Test signup form missing username - invalid
    def test_signup_form_missing_username(self):
        '''Test that the signup form is missing username'''
        form = UserCreationForm({
            'email': 'test_user@test.com',
            'password1': 'testpassword123#',
            'password2': 'testpassword123#',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    # Test signup form miss-matching passwords - invalid
    def test_signup_form_missmatching_passwords(self):
        '''Test that the signup form missmatching passwords'''
        form = UserCreationForm({
            'username': 'testuser',
            'email': 'test_user@test.com',
            'password1': 'testpassword123#',
            'password2': 'testpassword123',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'],
                                    ["The two password fields didn’t match."])

    # Test signup form missing password - invalid
    def test_signup_form_missing_password(self):
        '''Test that the signup form is missing password'''
        form = UserCreationForm({
            'username': 'testuser',
            'email': 'test_user@test.com',
            'password2': 'testpassword123#',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], ['This field is required.'])
