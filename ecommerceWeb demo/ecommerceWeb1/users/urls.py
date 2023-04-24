from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name = 'logout')
    # path('logout/', auth_view.LoginView.as_view(template_name = 'users/logout.html'), name='logout')
]