from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from putingoodhands.models import Donation, Institution, Category
from django.http import HttpResponse

# Create your views here.

class LandingPageView(View):
    
    def get(self, request):
        
        dontaions = Donation.objects.all()
        institutions = Institution.objects.all()
        
        return render(request,
                      'index.html',
                      {'institutions': institutions,
                       'dontaions': dontaions,
                       })
        
class LoginView(View):
    
    
    def get(self, request):
        return render(request,
                      'login.html')

    def post(self, request):
        
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        
        try:
            username = User.objects.get(email=email.lower())
        except:
            return redirect('register')
    
        user = authenticate(username=username, password=pwd)

        if user is not None:
            login(request, user)
        
        else:
            return redirect('login')
        
        return redirect('landing-page')

class RegisterView(View):
    
    def get(self, request):
        return render(request,
                      'register.html')
        
    def post(self, request):
        
        username = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        
        newuser = User.objects.create_user(
            username=username,
            email=email,
            password=pwd,
        )
        
        return render(request,
                      'login.html')
        

class AddDonation(View):
    
    def get(self, request):
        
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        
        return render(request,
                      'form.html',
                      {'categories': categories,
                       'institutions': institutions})

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('Wylogowano')