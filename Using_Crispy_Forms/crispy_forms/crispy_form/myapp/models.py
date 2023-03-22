from django.db import models

# Create your models here.
class Employees(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstname
    
    class Meta:
        verbose_name = 'Employees'
        verbose_name_plural = 'Employees'