from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return HttpResponse ("Welcome to my Blog!")

def about(request):
    context = {
        'my_name' : 'juweana',
        'my_age' : '28',
        'my_quote' : 'Be the change.',
        

    }
    return render (request, 'blog/about.html', context)

def hobbies (request):
    context ={
        'my_hobbies' : ['Coding','Painting','Reading','Travelling']
    }
    return render (request, 'blog/hobbies.html', context)

def post_list(request):
     posts = Post.objects.filter (is_published=True).order_by('-created_at')
     
     
     context = {
        'posts': posts,
    }

     return render(request, 'blog/post_list.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request,user)
            return redirect ('post_list')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})