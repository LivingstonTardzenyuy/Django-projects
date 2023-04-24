from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from myapp.models import *
from myapp.forms import *

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='login')
def items(request):
    items = Items.objects.all()

    context={
        'items':items,
    }
    return render(request, 'main/items.html', context)


def purchase_items(request, pk):
    return render(request, 'main/purchase_items.html')


def admin_dashboard(request):
    items =Items.objects.all()

    context ={
        'items': items,
    }
    return render(request, 'main/admin_dashboard.html', context)

def delete_product(request, pk):
    delete_item = Items.objects.get(id=pk)
    delete_item.delete()
    return redirect('admin_dashboard')


def add_products(request):
    form = Products()
    items = Items.objects.all()
    context={
        'form' : form,
        'items' : items
    }
    return render(request, 'main/add_products.html', context)