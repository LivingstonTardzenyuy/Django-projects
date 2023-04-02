from django.db import models
from django.contrib.auth.models import User

from django.core.validators import FileExtensionValidator           #to help only images to the uploaded no videos

# import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)       #becuase a user has only one profile
    image=models.ImageField(default='default.png', upload_to='media',
                            validators=[FileExtensionValidator(['png', 'jpg'])])
    
    
    # def __self__(self):
        # self.user.username
        
    # class Meta:
        # verbose_name = 'Profile'
        # verbose_name_plural = 'Profile'