from django.contrib import admin
from .models import Profile, Product, Category, Subscribstion

# Register your models here.

admin.site.register(Subscribstion)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
