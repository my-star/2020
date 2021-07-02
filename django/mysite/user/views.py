from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    # form = AuthenticationForm()
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            object= redirect('index')
            object.set_cookie("is_login",True)
            object.set_cookie("username",request.POST['username'])
            return object
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def index(request):

    return render(request,'index.html')