from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    blog=Blog.objects.all()

    # delete_blog=blog.delete()
    context={
        'blog':blog,
       
    }
    return render(request,'index.html', context)

def form(request):
    form=Input()
    if request.method=='POST':
        form=Input(request.POST)
        if form.is_valid():
            form=Reservation(name=request.POST['name'],
                             contact=request.POST['contact'], 
                             current_location=request.POST['current_location'], 
                             destination=request.POST['destination'], 
                             count=request.POST['count']
                             )
            if form.current_location != form.destination:
                form.save()
                return redirect('form')
            else:
                messages.info(request, "Your current location should be difference from destination location")
                return redirect('form')
    else:
        return render(request,'form.html',{'form':form})
    

def admin_site(request):
    form=Admin_site()
    backend=AdminLogin.objects.filter().first()
    if request.method == 'POST':
        form=Admin_site(request.POST) 
        if form.is_valid():
            form=AdminLogin(secret_login=request.POST['secret_login'])
            # form.save()
            if backend.secret_login == form.secret_login:
                # messages.success(request, 'Good welcome admin')
                return redirect('signin')
            
            else:

                messages.info(request, 'welcome admin')
                return redirect('/')
    
    return render(request, 'admins.html', {'form':form})


def admin_form(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('admin_form')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('admin_form')

            else:
                user= User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password1, email=email)
                user.save()
                return redirect('/')
                             
        
        else:
            messages.info(request, 'password should match')
            return redirect(request, 'admin_form')
    else:        
        return render(request, 'admin_form.html')


def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']

        user= auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            if username =='bamenda':
                
                return redirect('admin_bamenda')

            elif username=='buea':
                return redirect('admin_buea')
            elif username=='douala':
                return redirect('admin_douala')

            elif username=='yaounde':
                return redirect('admin_yaounde')

            else:
                return redirect('signin')
        
        
        else:
            messages.info(request,'credentials not valid')
    else:        
        return render(request, 'signin.html')
    
    
def admin_panel(request):
    reservation=Reservation.objects.filter()
    
    # if request.method == 'POST':
        
    return render(request, 'admin_panel.html', {'reservation': reservation})

def admin_bamenda(request):
    reservation= Reservation.objects.all()
    user=User.objects.get(username=request.user)
    # current_location=Reservation().objects.all()
    context={'user':user,'reservation':reservation}
    return render(request, 'admin_bamenda.html',context)

def admin_buea(request):
    reservation=Reservation.objects.all()

    user=User.objects.get(username=request.user)
    context={'user':user,'reservation':reservation}
    return render(request, 'admin_buea.html',context)

def admin_douala(request):
    reservation=Reservation.objects.all()
    user=User.objects.get(username=request.user)
    context={'user':user,'reservation':reservation}
    return render(request, 'admin_douala.html',context)

def admin_yaounde(request):
    user=User.objects.get(username=request.user)
    context={'user':user}
    return render(request, 'admin_yaounde.html',context)

def about(request):
    return redirect('/')

def bamenda_douala(request):
    reservation= Reservation.objects.all()
    user=User.objects.get(username=request.user)

    # current_location=Reservation().objects.all()
    context={'user':user,'reservation':reservation}
    return render(request,'bamenda_douala.html',context)

def bamenda_yaounde(request):
    reservation= Reservation.objects.all()
    user=User.objects.get(username=request.user)
    # current_location=Reservation().objects.all()
    context={'user':user,'reservation':reservation}
    return render(request,'bamenda_yaounde.html',context)

def bamenda_buea(request):
    reservation= Reservation.objects.all()
    user=User.objects.get(username=request.user)
    # current_location=Reservation().objects.all()
    context={'user':user,'reservation':reservation}
    return render(request,'bamenda_buea.html',context)


def blog(request):
    blogs= Blog.objects.all()
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            messages.info(request, 'Your form is not valid')
            return redirect('blog')
    else:
        form =BlogForm()
    context={
        'blogs':blogs,
        'form':form,
    }
    return render(request, 'blog.html', context)

def delete_blog(request, pk):
    blog_delete = Blog.objects.get(id=pk)
    blog_delete.delete()
    return redirect('blog')
    