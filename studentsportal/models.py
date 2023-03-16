from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'notes'
        verbose_name_plural = 'notes'


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField(default=datetime.now)
    is_finished = models.BooleanField(default=False)
    

    class Meta:
       
        verbose_name = 'homework'
        verbose_name_plural = 'homework'

    def __str__(self):
        return self.subject
    
class Todo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status =models.BooleanField(default=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'

    def __str__(self):
        return self.title
    



class Room(models.Model):
    name=models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Room'
    
class Message(models.Model):
    value = models.CharField(max_length=100000)
    date=models.DateTimeField(default= datetime.now, blank =True)
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=1000)


    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Message'




