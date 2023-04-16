from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

class Institution(models.Model):
    
    FUNDATION = 1
    NGO = 2
    LOCALCHARITY = 3
    TYPE_CHOICES = [
        (FUNDATION, 'Fundacja'),
        (NGO, 'Organizacja pozarządowa'),
        (LOCALCHARITY, 'Zbiórka lokalna'),
    ]
    
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=FUNDATION)
    categories =  models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
