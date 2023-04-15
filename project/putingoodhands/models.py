from django.db import models

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
