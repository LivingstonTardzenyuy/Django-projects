from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile_number = models.CharField(validators=[mobile_regex], max_length=17, blank=True)
    
    def __str__(self):
        return self.city
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discription = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='upload/')
    
    def __str__(self):
        self.name
class Subscribstion(models.Model):
    email = models.EmailField(max_length=50)
    