from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms
from base.forms import *
from base.models import *


# Create your views here.

def home(request):
    my_dict = {'insert_content':"If you already have account please login"}
    return render(request ,'base/home.html')

def people_view(request):
    details = st_details.objects.all()
    return render(request,'base/ppl.html',{'details':details})

def form_name (request):
    # ppl_list = people.objects.all().order_by('FirstName')
    # ppl_dict = {'people_access': ppl_list}
    # return render(request, 'base/ppl.html',context=ppl_dict)
    form = newuser()

    if request.method == 'POST':
        form = newuser(request.POST,request.FILES)

        if form.is_valid():
            form.save(commit=True)
            print("Your Response is Successfully recorded !!!")
            response = redirect('marks')
            return response
        
        else:
            print("Error! Form is Not submitted.")
    
    return render (request,'base/signup.html',{'form':form})
    
def marks_sheet(request):
    result = marksheet()

    if request.method == 'POST':
        result = marksheet(request.POST)

        if result.is_valid():
            result.save(commit=True)
            #return HttpResponse("<h1> Your response is recorded<h1>")
            return render(request,'base/tq.html')
        else:
            print("Error! Form is not submitted.")
    
    return render(request,'base/marks.html',{'marks':result})

def marks_view(request, id ):
    res = Marks.objects.all().filter(rollno=id)
    return render(request,'base/st_marks.html',{'res':res})

def search_venues(request):
    if request.method == 'POST':
        # searched= request.POST('searched')
        if 'CSE' in request.POST:
            search = st_details.objects.filter(Branch__contains = 'CSE')
        elif 'ECE' in request.POST:
            search = st_details.objects.filter(Branch__contains = 'ECE')
        elif 'IT' in request.POST:
            search = st_details.objects.filter(Branch__contains = 'IT')
        else:
            findout = request.POST['searched']
            if findout=="":
                search=[]
            else:
                search = st_details.objects.filter(rollno__contains = findout )
        # for i in search:
        #     print(i.Branch)
        return render(request, 'base/find.html',{'search':search})


