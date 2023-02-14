from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Features
from django.contrib.auth.models import User, auth  # the user is the one stored in our db, auth helps in authentifications
from django.contrib import messages


# Create your views here.
def index(request):
    feature=Features.objects.all()      #to get all data from our data base
    return render(request, 'index.html', {'features': feature})
    # return HttpResponse("hello world")

def register(request):
    if request.method=='POST':
        username=request.POST["username"]
        email=request.POST["email"]
        Password1=request.POST["Password1"]
        Password2=request.POST["Password2"]

        if Password1==Password2:
            if User.objects.filter(email = email).exists():  # checking if email exist in our db
                messages.info(request, 'Email already used')
                return redirect('register')
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            
            else:
                # we create user since the user does not exist
                user=user.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
                
        else:
            messages.info(request, "password not the same")
            return render(request, "register.html")

    else:
        return render(request, 'register.html')


def counter(request):
    text=request.POST['text']
    
    var1=len(text.split())
    context={
        'one':var1,
    }
    return render(request, 'counter.html', context)
    