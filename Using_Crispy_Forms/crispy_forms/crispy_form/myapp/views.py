from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    form=Registration(request.POST or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Registered!')
        return redirect('/')
    
    else:
        context={
            "form": form
        }
    return render(request, 'home.html', context)