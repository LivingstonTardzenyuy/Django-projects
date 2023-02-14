from django.db import models

# Create your models here.
class Features(models.Model):
    heading=models.CharField(max_length=50)
    details=models.CharField(max_length=200)
    