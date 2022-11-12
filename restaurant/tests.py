import email
from django.test import TestCase
from .models import Reservation
from .forms import BookingForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
# import unittest
from django.test import TestCase
from django.test import Client



if __name__ == '__main__':
    unittest.main()

# Test views
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", email="automated@test.com", password="testpassword"
        )
        self.user.save()
        self.reservation = Reservation.objects.create(
            user=self.user,
            first_name="test",
            last_name="user",
            email="automated@test.com",
            phone="+353123456789",
            reservation_date="2023-01-01",
            reservation_time="12:00",
            number_of_people=5,
        )
        self.reservation.save()

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_menu_page(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    def test_gallery_page(self):
        response = self.client.get(reverse("gallery"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery.html")

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_booking_page(self):
        response = self.client.get(reverse("booking"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking.html")

    def test_my_reservations_page(self):
        response = self.client.get(reverse("my_reservations"))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "login.html")

    def test_update_reservation_page(self):
        response = self.client.get(
            reverse("update_reservation", args=[self.reservation.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "login.html")

    def test_delete_reservation_page(self):
        response = self.client.get(
            reverse("delete_reservation", args=[self.reservation.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "login.html")

    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_logout_page(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "login.html")

    def test_register_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")


class TestForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="automated@test.com", password="testpassword"
        )
        self.user.save()

    def test_booking_form(self):
        form = BookingForm(
            {
                "first_name": "test",
                "last_name": "user",
                "email": "automated@test.com",
                "phone": "+353123456789",
                "reservation_date": "2023-01-01",
                "reservation_time": "12:00",
                "number_of_people": 5,
            }
        )

        self.assertTrue(form.is_valid())

    def test_booking_form_no_data(self):
        form = BookingForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)

    def test_booking_form_no_first_name(self):
        form = BookingForm(
            {
                "last_name": "user",
                "email": "automated@test.com",
                "phone": "+353123456789",
                "reservation_date": "2023-01-01",
                "reservation_time": "12:00",
                "number_of_people": 5,
            }
        )
