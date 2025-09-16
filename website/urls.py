from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('performances/', views.performances_page, name='performances'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('bookings/', views.bookings_page, name='bookings'),
    path('contact/', views.contact_page, name='contact'),
]


