#help us to great a profile for a user when he register authomatically

from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)