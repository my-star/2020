from django.views import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import UserLogin
from .models import User,Record,Log,Depart
from datetime import datetime,timedelta
class IndexView(View):
    def get(self,request):
        return redirect('/user/login/')

class LoginView(View):

    def get(self,request):
        if request.session.get('is_login',None):
            return redirect('/user/home/')
        login_form = UserLogin()
        return render(request,'login.html',locals())

    def post(self,request):
        login_form = UserLogin(request.POST)
        message = 'Please check input text'
        if login_form.is_valid():
            emp_num = login_form.cleaned_data['emp_num']
            password = login_form.cleaned_data['password']
            user = User.objects.filter(emp_num=emp_num,password=password).first()
            if user :
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                Log.objects.create(user=user,action='login')
                return redirect('/user/home/')
            else:
                message = 'Wrong Username or password!'
        return render(request,'login.html',locals())

class HomeView(View):

    def get(self,request):
        if not request.session.get('is_login',None):
            #messages.error(request,'Please,login')
            return redirect('/user/login/')

        records = Record.objects.order_by('-record_time')
        return render(request,'home.html', locals())
class LogoutView(View):

    def get(self,request):
        if request.session.get('is_login',None):
            user = User.objects.get(pk=request.session['user_id'])
            Log.objects.create(user = user,action='Logout')
            request.session.flush()
        return redirect('/user/login/')
