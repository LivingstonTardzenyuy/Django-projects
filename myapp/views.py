from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # context={
    #     "Name":"Kongnyuy",
    #     "age":19,
    #     "matricule":"UBa21E0027",
    # }
    return render(request, 'index.html')
    # return HttpResponse("hello world")

def counter(request):
    text=request.GET['text']
    var1=len(text.split())
    
    return render(request, 'counter.html',{'amount':var1})
    