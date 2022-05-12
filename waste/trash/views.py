
from django.http import HttpResponse
from django.shortcuts import render , redirect
from trash.forms import *
from trash import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.




# def home(request):
#     return HttpResponse("<h1>Hellow world ! your at Trash site....</h1>")

def home (request):
    return render(request, 'trash/home.html')


def registeration(request):

    regg = False 

    if request.method == 'POST':
        reg_form = registerationform (data = request.POST)

        if reg_form.is_valid():
           user = reg_form.save()
           user.set_password(user.password)
           user.save() 
           print ("Successfull registration")
           print(user)
           return HttpResponse("Thankyou for registering")
           regg = True 
        else:
            print(reg_form.errors)
    else:
        reg_form = registerationform()

    return render(request, 'trash/register.html', {'reg_form': reg_form})

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password = password)
        if user is not None:
            login(request, user)
            return HttpResponse("sucessfull login ")
        else:
            messages.success(request,("There was a problem login "))
            return render (request,'trash/login.html',{'message':'There was a problem login'})
    else:
        return render(request,'trash/login.html' )