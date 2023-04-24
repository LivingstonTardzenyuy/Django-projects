from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'