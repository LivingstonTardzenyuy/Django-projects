from django.shortcuts import render
from .models import Profiles
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getProfiles(request):
    content=Profiles.objects.all()
    return JsonResponse({"content": list(content.values())})
    
def create(request):
    if request.method=='POST':
        name=request.POST['name']
        bio=request.POST['bio']
        
        result=Profile(name=name, bio=bio)
        result.save()
        return HttpResponse("New profile created successfully")