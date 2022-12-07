from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Test login form
class TestForms(TestCase):
    """Test cases for the restaurant app"""

    # Test booking form for unauthenticated user,
    # user should be redirected to login page
    def test_booking_form_for_unauthenticated_user(self):
        """Test that the booking form is rendered"""
        response = self.client.get(reverse("booking"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/booking/")
        self.assertTemplateNotUsed(response, "booking.html")

    # Test booking form as valid authenticated user
    def test_booking_form_as_valid_authenticated_user(self):
        """Test that the booking form is rendered"""
        user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
        )
        self.client.force_login(user)
        response = self.client.get(reverse("booking"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking.html")
