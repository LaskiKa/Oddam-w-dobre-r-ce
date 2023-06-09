"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from putingoodhands.views import LandingPageView, LoginView, RegisterView, AddDonation, MyLogoutView, DonationConfirmationView
from putingoodhands.views import UserEditView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('adddonation/', AddDonation.as_view(), name='adddonation'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('confirmation/', DonationConfirmationView.as_view(), name='confirmation'),
    path('useredit/', UserEditView.as_view(), name='useredit')
    
]
