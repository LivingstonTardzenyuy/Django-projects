from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.views import generic
from .models import *
from youtubesearchpython import VideosSearch
import requests
from django.contrib.auth.decorators import login_required
import json
import wikipedia

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'Dashboard/home.html')

@login_required(login_url='login')
def notes(request):
    if request.method == 'POST':
        form=NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title = request.POST['title'],description = request.POST['description'])
            notes.save()
            return redirect('notes')
        messages.success(request,f"Notes added successfully by {request.user.username}")
    form = NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request, 'Dashboard/notes.html',context)

def note_detail(request,pk):
    
    notes=Notes.objects.get(id=pk)
    context={'notes':notes}
    return render(request, 'Dashboard/notes_detail.html',context)

@login_required(login_url='login')
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes

@login_required(login_url='login')
def homework(request):
    if request.method=="POST":


        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            homework = Homework(
                user=request.user,
                subject=request.POST['subject'],
                # due=request.POST['due'],
                title=request.POST['title'],
                description=request.POST['description'],
                is_finished=finished
            )
            homework.save()
            return redirect('homework')
            
        #     homework = Homework.objects(,)
        #     homework.save()
        #     return redirect('homework')
        else:
            messages.success(request,f'success')
    form = HomeworkForm()
    homework=Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homework':homework,'homework_done':homework_done,'form':form}
    return render(request, 'Dashboard/homework.html', context)

@login_required(login_url='login')
def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    
    return redirect('homework')

def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()

    return redirect('homework')

def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        
        result_list = []
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+=j['text']
                result_dict['descriptions']=desc
                result_list.append(result_dict)
                context ={
                    'form':form,
                    'results':result_list
                }
        return render(request,'Dashboard/youtube.html',context)
    else:
        form = DashboardForm
        context ={'form':form}
        return render(request,'Dashboard/youtube.html',context)

def todo(request):
    if request.method== 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['status']
                if finished == 'on':
                    finished=True
                else:
                    finished=False
                    # unfinished_todo=len(finished)
            except:
                finished=False

            todo = Todo(title = request.POST['title'],status = finished)
            todo.save()
            return redirect('todo')
        messages.success(request,f"Activity added successfully ")
    form = TodoForm()

    todo= Todo.objects.all()
    if len(todo) == 0:
        todo_done = True
    else:
        todo_done = False
        todo_length=len(todo)
    context= {
        'todo':todo,
        'form':form,
        'todo_done':todo_done,
        'todo_length':todo_length,
        'finished':todo_length,
    }
    return render(request, 'Dashboard/todo.html',context)


def delete_todo(request,pk=None):
    Todo.objects.filter(id=pk).delete()
    
    return redirect('todo')

def update_todo(request,pk=None):
    todo= Todo.objects.get(id=pk)
    if todo.status==True:
        todo.status=False
    else:
        todo.status=True
    todo.save()
    return redirect('todo')

def books(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r= requests.get(url)
        answer=r.json()
        result_list = []
        for i in range(10):
            result_dict={
              
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            result_list.append(result_dict)
        
            context ={
                   
                    'results':result_list
                }
        return render(request,'Dashboard/books.html',context)
    else:
     form = DashboardForm
     context ={'form':form}
    return render(request,'Dashboard/books.html',context)
def dictionary(request):
    if request.method == 'POST':
        form= DashboardForm(request.POST)
        text = request.POST['text']
        
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r=requests.get(url)
        answer=r.json()
        try:
            
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definition'][0]['synonyms']
            context ={
                'form':form,
                'input': text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context={
                'form':form,
                'input':''
            }
        return render(request, 'Dashboard/dictionary.html',context)
    else:
        form=DashboardForm()
        context = {'form':form}
        return render(request,'Dashboard/dictionary.html',context)

def wiki(request):
    if  request.method =="POST":
        text=request.POST['text']
        form=DashboardForm(request.POST)
        search=wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary

        }
        return render(request, 'Dashboard/wiki.html',context)
    else:
        form=DashboardForm()
        context={
            'form':form
        }
    return render(request, 'Dashboard/wiki.html',context)

def conversion(request):
    if request.method=="POST":
        form=ConversionForm(request.POST)
        if request.POST['measurement']=='length':
            measurement_form=ConversionLengthForm()
            context={
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input)>=0:
                    if first == 'yard' and second== 'foot':
                        answer = f'{input} yard={int(input)*3} foot'

                    if first == 'foot' and second== 'yard':
                        answer = f'{input} foot={int(input)/3} yard'
                    context= {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer
                    }
        if request.POST['measurement'] == 'mass':
            measurement_form=ConversionLengthForm()
            context={
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input)>=0:
                    if first == 'pound' and second== 'kilogram':
                        answer = f'{input} pound ={int(input)*0.453592} kilogram'

                    if first == 'kilogram' and second== 'pound':
                        answer = f'{input} kilogram={int(input)*2.20462} pound'
                    context= {
                        'form':form,
                        'm_form':measurement_form,
                        'input':True,
                        'answer':answer
                    }
    form = ConversionForm()
    context={'form':form,'input':False}
    return render(request,'Dashboard/conversion.html',context)



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('login')
    else:
           
        return render(request,'Dashboard/register.html')

def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials invalid")
            return redirect('login')
    else:
        return render(request,'Dashboard/login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request):
    homeworks=Homework.objects.filter(is_finished=False,user=request.user)
    todos= Todo.objects.filter(status=False)
    if len(homeworks)==0:
        homework_done = True
    else:
        homework_done = False
    if len(todos)==0:
        todos_done = True
    else:
        todos_done = False
    context={
        'homeworks':homeworks,
        'todos':todos,
        'homework_done':homework_done,
        'todos_done':todos_done
    }
    return render(request,'Dashboard/profile.html',context)


def chat(request):
    return render(request, 'chats/chat.html')

def room(request, room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    
    context ={
        
        
        
    }
    return render(request, 'chats/room.html',{
        'username': username,
        'room_details': room_details,
        'room' : room,
    
    })

def checkview(request):
    room = request.POST['room_name']
    username=request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('chats/room' + room + '/username?=' + username )
    else:
        roomName=Room.objects.create(name=room)
        roomName.save()
        return redirect('chats/room' + room + '/username?=' + username )
        
        