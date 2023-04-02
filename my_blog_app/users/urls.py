from django.urls import path
from . import views


from django.contrib.auth import views as auth_view      # to help us us class base views


urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    #reseting password
    path('password_reset', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset_done', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb65>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    ]
