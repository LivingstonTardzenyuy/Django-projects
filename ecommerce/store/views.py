from django.shortcuts import render,HttpResponse,redirect
from .models import Subscribstion,Product
from django.contrib.auth.hashers import make_password,check_password
from . forms import User_signup, Profile_page
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = User_signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = User_signup()
    
    context = {
        'form':form
    }
    return render(request,'signup.html', context)

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')



@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = Profile_page(request.POST)
        if form.is_valid():
            u_form =User_signup(request.POST or None, instance = request.user) 
            if u_form.is_valid():
                u_form.save()
                return redirect('profile')        
    else:
        u_form = Profile_page(instance = request.user)
    
    context={
        'form': u_form
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def home ( request):
    return render (request,'index.html')


@login_required(login_url='login')
def electronic(request):
    return render (request,'electronic.html')

def fashion(request):
    fashion=Product.objects.all()
    return render (request,'fashion.html',{'fashion':fashion})

def jewellery(request):
    return render (request,'jewellery.html')

def cart(request):
    return render (request,'cart.html')


        

def subscribstion(request):
 if request.method == 'POST':
    email=request.POST['Email']
    
    if Subscribstion.objects.filter(email=email):

        msg='you already SUBSCRIBEED...!'
        return render (request,'index.html',{'msg':msg})
    else:
        Subscribstion(email=email).save()
        msg='Thanks for SUBSCRIBE...!'
        return render (request,'index.html',{'msg':msg}) 