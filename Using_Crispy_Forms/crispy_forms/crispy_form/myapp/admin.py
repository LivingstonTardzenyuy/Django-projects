from django.contrib import admin

# Register your models here.
from .models import *


class EmployeesAdmin(admin.ModelAdmin):
    list_display=['firstname', 'lastname', 'email']
    search_fields=['firstname', 'lastname', 'email']
    list_per_page=10

admin.site.register(Employees, EmployeesAdmin)