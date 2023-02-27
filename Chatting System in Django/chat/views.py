from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username=request.GET.get('username')            #to get the username
    room_details=Room.objects.get(name=room)
    # value=request.GET.get('value')
    details={
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'room.html', details)

def checkview(request):
    username=request.POST['username']
    room=request.POST['room_name']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    
    else:
        createRoom=Room.objects.create(name=room)
        createRoom.save()
        return redirect('/'+room+'/?username='+username)    
    
def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']
    
    new_message=Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message was successfully sent")



def getMessages(request, room):
    room_details=Room.objects.get(name=room)
    
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(messages.values())})