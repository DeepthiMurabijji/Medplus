from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    my_dict = {'insert_me': "Hello i am from views.py!"}
    return render(request,'polls/index.html',context = my_dict)