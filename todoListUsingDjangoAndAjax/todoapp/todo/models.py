from django.db import models

# Create your models here.
class Profiles(models.Model):
    name=models.CharField(max_length=50)
    text=models.TextField()
    bio=models.CharField(max_length=50)
    
    def __init(self):
        self.name=name