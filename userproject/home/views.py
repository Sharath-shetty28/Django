from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    render(request,'index.html')

def logout(request):
    render(request,'index.html')

def login(request):
    render(request,'login.html')