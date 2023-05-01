from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from putingoodhands.models import Donation, Institution, Category
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

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
        

class AddDonation(LoginRequiredMixin, View):
    
    def get(self, request):
        
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        
        return render(request,
                      'form.html',
                      {'categories': categories,
                       'institutions': institutions})
        
    def post(self, request):
        
        print(request.POST)
        
        categories_name = request.POST.get('categories')
        categories = Category.objects.get(name=categories_name)
        quantity = request.POST.get('quantity')
        organization_id = request.POST.get('organization')
        institution = Institution.objects.get(pk=organization_id)
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        more_info = request.POST.get('more_info')
        user_id = request.POST.get('user')
        user = User.objects.get(pk=user_id)
        
        
        donation = Donation.objects.create(
            quantity=quantity,
            institution=institution,
            address=address,
            phone_number=phone,
            city=city,
            zip_code=postcode,
            pick_up_date=date,
            pick_up_time=time,
            pick_up_comment=more_info,
            user=user
        )
        
        donation.categories.add(categories)
        
        return redirect('confirmation')

class DonationConfirmationView(View):
    
    def get(self, request):
        return render(request,
                      'form-confirmation.html')
        
        

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('Wylogowano')
    
class UserEditView(View):
    
    def get(self, request):
        return render(request,
                      'user-edit-form.html')
        
    def post(self, request):
                
        firstname = request.POST.get("username")
        lastname = request.POST.get("surname")
        username = request.POST.get('login')
        
        user = User.objects.get(pk=self.request.user.id)
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        
        user.save()
        
        return redirect('useredit')
