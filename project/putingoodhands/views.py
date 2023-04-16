from django.shortcuts import render
from django.views import View
from putingoodhands.models import Donation, Institution

# Create your views here.

class LandingPageView(View):
    
    def get(self, request):
        
        dontaion = Donation.objects.all()
        institution = Institution.objects.all()
        
        return render(request,
                      'index.html',
                      {'institution': institution,
                       'dontaion': dontaion})
        
class LoginView(View):
    
    def get(self, request):
        return render(request,
                      'login.html')


class RegisterView(View):
    
    def get(self, request):
        return render(request,
                      'register.html')
        

class AddDonation(View):
    
    def get(self, request):
        return render(request,
                      'form.html')
        