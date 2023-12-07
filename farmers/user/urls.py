from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    # Your other views and paths go here
    path('', Register, name='register'),
    path('login/', Login, name='login'),
    # Example: Include Django authentication URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # You can include more authentication-related URLs as needed
    path('password_reset/', include('django.contrib.auth.urls')),
]
