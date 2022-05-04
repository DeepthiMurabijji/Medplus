from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request,'supply/home.html')


def userlogin(request,role):
    if request.method=="POST":
        if request.POST['role']=='manager':
            obj = Manager.objects.filter(Q(user_name=request.POST['usr']) & Q(password=request.POST['psw']))
            print(obj)
            if len(obj)==0:
                print("Manager Name or the Password is Wrong")
                return HttpResponse("Invalid user name or password")
            else:
                print("Successful Manager Login")
                return render(request,'supply/dashboardman.html',{'user':request.POST['usr']})
        elif request.POST['role']=='user':
            obj = SupplyUser.objects.filter(user_name=request.POST['usr']).filter(password=request.POST['psw'])
            print(obj,len(obj))
            print("hello")
            if len(obj)==0:
                print("User Name or the Password is Wrong")
                return HttpResponse("Invalid user name or password")
            else:
                print("Successful User Login")
                return render(request,'supply/dashboarduser.html',{'user':request.POST['usr']})
    return render(request,'supply/login.html',{'role':role})

def register(request,role):
    if request.method=="POST":
        if request.POST['role']=='manager':
            form = Manager(first_name=request.POST['firstname'], last_name=request.POST['lastname'],
                        gender=request.POST['gender'], address=request.POST['address'],
                        user_name=request.POST['username'], email=request.POST['email'], password=request.POST['psw'],
                        phone=request.POST['phone'], rpassword=request.POST['psw-repeat'])
            try:
                form.save()
                print("Manager here")
                return render(request,'supply/dashboardman.html',{'user':request.POST['username']})
            except:
                return HttpResponse("Form Invalid")
        elif request.POST['role']=='user':
            form = SupplyUser(first_name=request.POST['firstname'], last_name=request.POST['lastname'],
                        gender=request.POST['gender'], address=request.POST['address'],
                        user_name=request.POST['username'], email=request.POST['email'], password=request.POST['psw'],
                        phone=request.POST['phone'], rpassword=request.POST['psw-repeat'])
            try:
                form.save()
                print("User Here")
                return render(request,'supply/dashboarduser.html',{'user':request.POST['username']})
            except:
                return HttpResponse("Form Invalid")
        else:
            return HttpResponse("Please select valid option")
    else:
        return render(request, 'supply/register.html',{'role':role})

def products(request):
    return render(request, 'products.html')

def managerprofile(request):
    return render (request, "managerprofile.html")