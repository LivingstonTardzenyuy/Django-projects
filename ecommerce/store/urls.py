from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,name='index'),
    path('electronic', views.electronic,name='electronic'),
    path('fashion', views.fashion,name='fashion'),
    path('jewellery', views.jewellery,name='jewellery'),
    path('cart', views.cart,name='cart'),
    path('subscribstion', views.subscribstion,name='subscribstion'),
    path('logout', views.logout, name='logout'),
    
    
    #users login
    path('signup/', views.signup,name='signup'),
    path('login', auth_views.LoginView.as_view(template_name ='login.html') ,name='login'),
    path('profile', views.profile, name='profile'),
    
    path('password_reset', auth_views.PasswordResetView.as_view(template_name ='password_reset.html') ,name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name ='password_reset_done.html') ,name='password_reset_done'),
    path('password_reset_confirm/<uidb65>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ='password_reset_confirm.html') ,name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name ='password_reset_complete.html') ,name='PasswordResetConfirmView'),
]
