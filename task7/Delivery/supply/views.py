from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'supply/home.html')


def userlogin(request):
    return render(request,'supply/login.html')

def register(request):
    return render(request, 'supply/register.html')