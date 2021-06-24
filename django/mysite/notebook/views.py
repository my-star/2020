from django.shortcuts import render
from django.http import HttpResponse
from notebook.models import User,Depart,Record
# Create your views here.

def index(request):
    records = Record.objects.all()
    context ={
        "records":records
    }
    return render(request,"record_list.html",context)