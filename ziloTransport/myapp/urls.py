from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('form',views.form,name='form'),
    # path('register',views.register,name='register'),
    path('admin_site', views.admin_site, name='admin_site'),
    path('admin_form', views.admin_form, name='admin_form'),
    path('signin', views.signin, name='signin'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('admin_bamenda', views.admin_bamenda, name='admin_bamenda'),
    path('admin_buea', views.admin_buea, name='admin_buea'),
    path('admin_yaounde', views.admin_yaounde, name='admin_yaounde'),
    path('admin_douala', views.admin_douala, name='admin_douala'),
    path('about', views.about, name='about'),
    path('bamenda_douala', views.bamenda_douala, name='bamenda_douala'),
    path('bamenda_yaounde', views.bamenda_yaounde, name='bamenda_yaounde'),
    path('bamenda_buea', views.bamenda_buea, name='bamenda_buea'),    
    path('blog', views.blog, name='blog'),    
    path('delete_blog<pk>', views.delete_blog, name="delete_blog"),

]
