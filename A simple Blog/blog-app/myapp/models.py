from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=5000)
    created_at=models.DateTimeField(default= datetime.now, blank=True)
    
class signIn(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)