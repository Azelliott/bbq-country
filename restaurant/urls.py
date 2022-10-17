from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu/', views.MenuPage.as_view(), name='menu'),
    path('gallery/', views.GalleryPage.as_view(), name='gallery'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path ('booking/', views.BookingPage.as_view(), name='booking'),
    path ('my_reservations/', views.MyReservationsPage.as_view(), name='my_reservations'),
    path ('update_reservation/<str:pk>/', views.update_reservation, name='update_reservation'),
    path ('delete_reservation/<str:pk>/', views.delete_reservation, name='delete_reservation'),
]