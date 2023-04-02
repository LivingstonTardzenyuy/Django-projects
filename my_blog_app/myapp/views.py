from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import PostFormModel, EditPost, CommentsForm

from django.contrib.auth.decorators import  login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form=PostFormModel(request.POST)
        
        if form.is_valid():
            instance=form.save(commit=False)     #get the data but dont save
            instance.author=request.user
            instance.save()
            return redirect('index')
    else:
        form=PostFormModel()
    postModel_object=PostModel.objects.all()
    
    return render(request, 'myapp/index.html', {'postModel_object':postModel_object, 'form':form})


@login_required(login_url='login')
def postDetails(request,pk):
    post=PostModel.objects.get(id=pk)
    
    if request.method == 'POST':
        form= CommentsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            intance.user = request.user             #assign user and author 
            instance.post = post
            instance.save()
            return redirect('postDetails', pk=post.id)
            # form.save()
        
    else:
        form= CommentsForm()
    context={                                                                                         
        'p_details':post,
        'form': form,
    }
    return render(request, 'myapp/postDetails.html', context)

@login_required(login_url='login')
def edit_post(request, pk):
    post=PostModel.objects.get(id=pk)
    
    if request.method == 'POST':
        form=EditPost(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('postDetails', pk=post.id)
    else:
        form=EditPost(instance=post)
    
    context={
        "post":post,
        'form':form,
    }
    
    return render(request, 'myapp/edit_post.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    delete_p = PostModel.objects.filter(id=pk).first()
    delete_p.delete()
    return redirect('index')
    # return render(request, 'myapp/delete_post.html')
    