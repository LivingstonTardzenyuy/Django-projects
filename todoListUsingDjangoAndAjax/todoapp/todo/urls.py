from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getProfiles', views.getProfiles, name='getProfiles'),
    path('create', views.create, name='create')
    
]
