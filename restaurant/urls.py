from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu/', views.MenuPage.as_view(), name='menu'),
    path('gallery/', views.GalleryPage.as_view(), name='gallery'),
    #path('about/', views.AboutPage.as_view(), name='about'),
    #path ('booking/', views.BookingPage.as_view(), name='booking'),
]