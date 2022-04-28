from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    return render(request,'polls/home.html')

def index(request):
    my_dict = {'insert_me': "Hello i am from views.py!"}
    return render(request,'polls/index.html',context = my_dict)

def myform(request):
     

    # form = newuser()
    # if request.method =='POST':
    #     form = newuser(request.POST,request.FILES)

    #     if form.is_vaild():
    #         form.save(commit=True)
    #         print("your response recored")
    #         return HttpResponse("form sucessfully submitted")

    #     else:
    #         print("Error!")
    #         return HttpResponse("Error! ocucured")
    print(request.GET)

    return render(request,'polls/form.html')
