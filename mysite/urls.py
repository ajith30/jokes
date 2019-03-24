from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('contact/', views.Contact.as_view(), name ='contact'),
    path('contact/', views.contact, name='contact'),
    path('thank/', views.thank_you, name='thank_you'),
    path('portfolio/', views.portfolio, name="portfolio")
]
