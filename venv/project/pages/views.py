from django.shortcuts import render

# Create your views here.

def index(request):
    x= {'name':'abdullatif', "age":'27'} 
    return render(request,'pages/index.html',x)

def about(request):
    return render(request,'pages/about.html')

def login(request):
    return render(request,'pages/login.html')

def register(request):
    return render(request,'pages/register.html')