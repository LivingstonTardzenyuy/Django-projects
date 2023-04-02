from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import  SignUp_form
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.decorators import login_required
from . forms import SignUp_form, Profileprofileupdate, UserProfileUpdate

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form=SignUp_form(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('profile')
    else: 
        form=SignUp_form()
    
    
    context={
        'form':form
        }
    return render(request, 'users/sign_up.html', context)

@login_required(login_url='/')
def profile(request):
    # user_profile= User.objects.all()
    # post_profile= Profile.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        u_form = UserProfileUpdate(request.POST or None, instance= request.user)            #or None simple handle the fact when the user has no profile yet
        p_form = Profileprofileupdate(request.POST or None, request.FILES or None, instance= request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            # p_form.save()
            return redirect('profile')
    else:
        u_form = UserProfileUpdate(instance = request.user)
        p_form= Profileprofileupdate(instance = request.user.profile)
    
    context ={
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request, 'users/profile.html', context)