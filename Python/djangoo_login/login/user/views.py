from django.shortcuts import render,redirect
from .forms import userlogin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import MatUser,Department,Computer
# Create your views here.
def acc_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
    else:
        form = userlogin()
    return render(request,'login.html',{'form':form})
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def acc_logout(request):
    logout(request)
    return redirect('/user/login/')

@login_required
def com_list(request):
    computers = Computer.objects.all()
    context= {
        'computers':computers
    }
    return render(request,'computer_list.html',context)

