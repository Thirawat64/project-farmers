from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('home', home, name='home'),
    path('about/', About, name='about'),
    path('help/', Help, name='help'),
    path('contact/', contact, name='contact'),
]