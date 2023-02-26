from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# from django.contrib.auth import auth_views
from django.contrib.auth.models import User, auth
from django.contrib import messages


from .models import Post, signIn

# Create your views here.

def index(request):
    posts=Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
 
def post(request, pk):
    posts=Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

def signUp(request):
    return render(request, 'signUp.html')


def signIn(request):
    if request.method=='POST':
        username=request.POST['username'] 
        password=request.POST['password']
        
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "credential not satisfied")
            return redirect('signIn')

    return render(request, 'signIn.html')

def signUp(request):
    if request.method=="POST":
            
        fullNames=request.POST['fullNames']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, 'signUp')
            
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return render(request, 'signUp')
        
            else:
                user=User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('signIn')
        else:
            messages.info(request, 'password does not match')
            return redirect('signUp')    
    else:
        return render(request, 'signUp.html')        
        