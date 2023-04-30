
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
towns=(
    ("Bamenda","Bamenda"),
    ("Douala","Douala"),
    ("Yaounde", "Yaounde"),
    ("Buea", "Buea"),
)
time=(("4pm","4pm"),("12pm","12pm"))
class Reservation(models.Model):
    name=models.CharField(max_length=100, blank=False)
    contact= models.CharField('phone number',max_length=15)
    current_location=models.CharField(max_length=30,choices=towns,default='Bamenda')
    destination=models.CharField(max_length=30,choices=towns,default='Douala')
    TravelTime=models.CharField(max_length=30,choices=time,default='4pm')
    count=models.IntegerField()
    notes=models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservation'

class AdminLogin(models.Model):
    secret_login=models.CharField(max_length=50)
    
    def __str__(self):
        return self.secret_login
    
    class Meta:
        verbose_name = 'AdminLogin'
        verbose_name_plural = 'AdminLogin'
        
class Manager(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField('phone number', max_length=15)
    email=models.CharField(max_length=50)
    current_location=models.CharField(max_length=30,choices=towns)
    destination=models.CharField(max_length=30,choices=towns,default='Bamenda')
    password=models.CharField(max_length = 150)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Manager'
        

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media')
    datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'