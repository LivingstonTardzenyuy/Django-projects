from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Comment)

class PostModelAdmin(admin.ModelAdmin):
    list_display=('title', 'content', 'date_created')
admin.site.register(PostModel, PostModelAdmin)
