from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from putingoodhands.models import Donation, Institution, Category

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
        