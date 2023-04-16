from django.shortcuts import render
from django.views import View
from putingoodhands.models import Donation, Institution, Category

# Create your views here.

class LandingPageView(View):
    
    def get(self, request):
        
        dontaions = Donation.objects.all()
        institutions = Institution.objects.all()
        # institutionscategories = Category.objects.all()
        for i in institutions:
            print(i.name)
            print(i.description)
            print(i.categories)        
        
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
        

class AddDonation(View):
    
    def get(self, request):
        return render(request,
                      'form.html')
        