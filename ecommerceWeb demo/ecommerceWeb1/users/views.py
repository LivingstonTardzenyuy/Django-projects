from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'The username already exists')
                return redirect('sign_up')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'The email already exists')
                return redirect('sign_up')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email)
                user.save()

                return redirect('login')
        else:
            messages.info(request, 'The two Passwords do not match')
            return redirect('sign_up')
    else:
        return render(request, 'users/sign_up.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials are invalid')
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')