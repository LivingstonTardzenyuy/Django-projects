from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    if request.method=="POST":
        text=request.POST['text']
        amount_of_word=len(text.split())
        return render(request, 'counter.html', {'total': amount_of_word})
        # return render(request, 'counter.html')
    return render(request,'counter.html')