

from datetime import datetime as dt
from dbm import error
from email import header
from gc import collect
from django.db.models import Q
from django.utils.functional import SimpleLazyObject
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from numpy import true_divide
from pyparsing import col
from trash.models import *
from django.contrib import messages 
from django.urls import reverse
from django.template.loader import get_template
import csv
from fileinput import filename
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from django.utils import timezone
import datetime



# Create your views here.

global registerKey
registerKey = False

global adminKey
adminKey = False

global memberkey 
memeberkey = False

def home(request):
    context={}
    registerKey = False

    if request.user.is_authenticated:
        # print("Active status here",request.user.is_active)
        username = request.user.username  
        context={
        'username': username,
        }
    else:
        registerKey = False
    
        context={
            'registerKey':registerKey,
        }
     
    return render(request, 'home.html', context)


def register(request):

    areas = Areas.objects.all()
    context = {'areas': areas}

    return render(request, 'register.html', context)

data = [['Garbage Collector','Houses Cleaned','Date and Time']]

def create_csv_file(request):
    global data
    response =HttpResponse(content_type='text/csv')
    write = csv.writer(response)
    for i in data:
        write.writerow(i)
    response['Content-Disposition'] ='attachment; filename= "work.csv"'
    return response
# TODO:  FOR  REST API DJANGO 
@csrf_exempt
@api_view(['GET', 'POST'])
def apiRegister(request):


    if request.method == 'POST':
        userData = JSONParser().parse(request)
        

        username = userData.get('username')
        #print("hi",username)
        email = userData.get('email')
        #print(email)
        password = userData.get('password')
        #print(password)
        areas = userData.get('areas')
        #print(areas )
    
        # user = User.objects.get(username = username)
        user = User.objects.create_user(username = username, email = email)
        areaObject = Areas.objects.get(area_name = areas)

        collector = Collector()

        user.set_password(password)
        user.save()
        collector.area = areaObject
        collector.user = user
        collector.save()

        return JsonResponse("Collector Saved!", safe=False)

    elif request.method == "GET":

        areas = Areas.objects.all()
        areasSerial = AreaSerializer(areas, many = True)

        #print(areasSerial.data)

        return JsonResponse(areasSerial.data, safe = False)

@csrf_exempt
@api_view(['POST' , 'GET'])
def apiLogin(request):
    # print("request" ,request.method)
    if request.method == 'POST':
        loginData = JSONParser().parse(request)
        #print(loginData)
        user_name = loginData['username']
        password = loginData['password']
        # print("hello" ,user_name, password)


        try:
            user = User.objects.get(username = user_name)
            collector = Collector.objects.get(user = user)
            loginSerial =  Collectorserializer(collector)
            # print("----serializers----")
            # print(loginSerial.data)
        except User.DoesNotExist:
            return JsonResponse({"Msg": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


        authuser = authenticate(username = user_name, password = password)
        print("Authentication Token",authuser)
        # collector = Collector.objects.get(user = user)
        houses = Houses.objects.filter(area = collector.area)

        # if authuser is None:

        #     raise exceptions('Try again')

        if authuser != None:
            if collector.is_real == True:
                login(request, authuser)
                return JsonResponse(loginSerial.data, safe=False)
            else :
                return JsonResponse({"Msg":'Your is not Activated'},status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({"Msg": "Wrong password"}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST' , 'GET' ])
def apiArealist(request):
    if  request.method == 'GET':
        # print(".........Please enter...........")
        areas = Areas.objects.all()
        houses = Houses.objects.all()
        houseserial = Houseserializer(houses, many = True)
        areaserial = AreaSerializer(areas , many = True)

        returnDict = {}

        for area in areas:
            
            x = Areas.objects.get(area_name = area)
            housesCount = Houses.objects.filter(area = x).count()

            returnDict[x.area_name] = housesCount + 1       

        #print(returnDict)

        #print('houses:',houseserial.data)

    #print(type(returnDict))

    response = Response()

    response.data = {
        'houses': houseserial.data, 'houseCount': returnDict ,'areas': areaserial.data
    }

    return response


@csrf_exempt
@api_view(['POST', 'GET'])
def apiarearegistration(request):
    if request.method == 'POST':
        areaData = JSONParser().parse(request)
        areaname = areaData['areaname']
        housename = areaData['housename']
        houseaddress = areaData['address']
        print("!!!!", areaData)
        house = Houses()
        if (Areas.objects.filter(area_name=areaname).exists()):
            print("area name already exists", areaname)
            if(Houses.objects.filter(house_name=housename).exists()):
                print("house name already exists", housename)
                return JsonResponse({'msg' : 'house name already exists'} , safe = False)
            else:
                house.area = Areas.objects.get(area_name=areaname)
                house.house_name = housename
                house.house_address = houseaddress
                house.save()
                print("saved house")
                return JsonResponse({'msg' : 'saved house'} , safe = False)
        elif(Areas.objects.filter(area_name=areaname).exists() == False):
            
            print("new Area name", areaname)
            area = Areas()
            area.area_name = areaname
            area.save()
            
            house.area = area
            house.house_name = housename
            house.house_address = houseaddress
            house.save()
            print("registred")
        else:
            return JsonResponse({'Msg:': "string is empty"} , status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse("oops errors", safe = False)
    # elif request.method == 'GET':
    #     areas = Areas.objects.all()
    #     areasSerial = AreaSerializer(areas, many = True)
    #     return JsonResponse(areasSerial.data, safe = False)

@csrf_exempt
@api_view(['POST','GET'])
def apiAdministration(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        print("hi")
        collectors = Collector.objects.all()
        collector_serializer = Collectorserializer(collectors, many = True)
        home = Houses.objects.all()
        house_serializer = Houseserializer(home, many = True)
        areas = Areas.objects.all()
        area_serializer = AreaSerializer(areas, many = True)
        mainview = []
        collectorhouses ={}
        for collector in collectors:
            houses = Houses.objects.filter(area = collector.area)
            
            
            hoselist = []
            hoseadd = []
            for house in houses:
                hoselist.append(house.house_name)
                hoseadd.append(house.house_address)
            collectorhouses[collector.user.username] = hoselist
            # mainview.append(collectorhouses)
        # print(mainview)  
        print(timezone.now())  # The UTC time   2022-07-15 06:57:05.430490+00:00
        print(timezone.localtime())  # timezone specified time,if timezone is UTC, it is same as above  2022-07-15 12:27:05.430538+05:30
        print("I think this is right",datetime.datetime.now())  #2022-07-15 12:27:05.430584
        print(datetime.datetime.now().date())
       
        response = Response()

    response.data = {
        'mainview': collectorhouses, 'collector_serializer':collector_serializer.data, 'home': house_serializer.data
    }

    return response       
       
         
    return JsonResponse(collectorhouses, safe = False)

@csrf_exempt
@api_view(['POST' , 'GET'])
def apiEditing(request):
    
    if request.method == 'GET':
        id = request.GET.get('id')
        #print( "id",id)
        user = User.objects.get(id = id)
        # collector = list(Collector.objects.filter(user_id = user).values())
        # print(collector[0])
        # collector = collector[0]
        collector = Collector.objects.filter(user_id = user)
        # print(collector)
        collectorserial = Collectorserializer(collector , many = True)
        # print(collectorserial.data)
        return JsonResponse(collectorserial.data[0] , safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        print(user_data)
        # user = User.objects.get(id = user_data.get('user'))
        collector = Collector.objects.filter(id = user_data.get('id'))
        # data = Collector.objects.filter(user_id = user_data.get('user')['id']).update()
        collector.update(is_admin=user_data['is_admin'],is_real = user_data['is_real'])
        # print('data', collector.is_admin, type(collector))
        return JsonResponse( user_data,safe=False)


@csrf_exempt
@api_view(['POST' , 'GET'])
def apiMember(request):
    if request.method == 'POST':
        usr =  request.GET.get('member')
        # print("user name: ", usr)
        checkedHouses = JSONParser().parse(request)
        # print("Houses checked: ",checkedHouses)
        user = User.objects.get(username = usr)
        collector = Collector.objects.get(user = user)
        housesTable = Houses.objects.filter(area = collector.area)
        for house in housesTable:
            for item in checkedHouses:
                if(house.house_name == item):
                    #print("Houses checked", house.house_name, item)
                    house.is_completed = 'Completed'
                    house.collector = collector 
                    house.save()
                    activity_log = ActivityLog.objects.create(
                        collector = collector, houses = house, time = str(dt.now())[11:19]
                        )
                    activity_log.save()
        return JsonResponse("Members Houses Checked" , safe=False)
    elif request.method == 'GET':
        usr =  request.GET.get('member')
        # print(usr)
        user = User.objects.get(username = usr)
        collector = Collector.objects.get(user = user)
        collectorserial = Collectorserializer(collector)
        # print('collector', collectorserial)
        area = Areas.objects.get(id = collector.area_id)
        # print(area)
        home = Houses.objects.filter(area_id = area.id)
        # print('home', home)
        homeserial = Houseserializer(home, many = True)
        #print(homeserial.data)
        # datetime.now()
        # now = datetime.now()
        # print("date.today() is",date.today())
        # print("The time Zone Time is :",now)
        # print("The Date is :",str(now)[:10])
        # print("The Time is :",str(now)[11:19])
        return JsonResponse(homeserial.data , safe = False)

@csrf_exempt
@api_view(['POST', 'GET'])
def apiResetButton(request):
    houses_chk = Houses.objects.all()
    collectors =Collector.objects.all()
    for i in collectors:
        i.area_status = False
        i.save()
    for i in houses_chk:
        print(i.is_completed,type(i.is_completed))
        i.is_completed = 'Not Completed'
        i.collector = None
        i.save()
        print("Status changed to false")
    return JsonResponse("Successfully Reset" , safe = False)  
        

# @csrf_exempt
def register_save(request):

    areas = Areas.objects.all()

    if request.method == 'POST':

#         #region........connect to frontend 
#         collector_data = JSONParser.parse(request)
#         collector_serializer = Collectorserializer(data= collector_data)
#         if collector_serializer.is_valid():
#             collector_serializer.save()
#             return JsonResponse("Successfully registered" , safe=False)
#         return JsonResponse("Failed to register")
#         #region

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        areas = Areas.objects.get(area_name = request.POST.get('area')) 

        if password == password1:

            if (User.objects.filter(username=username).exists()):
                print("username already exists")
                areas = Areas.objects.all()

                context = {
                            'areas': areas,
                            'name': 'User already exists try another',
                }
                return render(request, 'register.html',context)  
            else:
                # user = User.objects.create_user(username = username,email = email)

                if (User.objects.filter(email = email).exists()):
                    # print("email already exists")
                    areas = Areas.objects.all()

                    context = {
                        'areas': areas,
                        'email': 'Email already exists try another',
                    }
                    return render(request, 'register.html', context)  
                else:
                    user = User.objects.create_user(username = username,email = email)

        
            user.set_password(password)
            user.save()

            collector = Collector()

            collector.user = user
            collector.area = areas
            collector.is_admin = False
            collector.area_status = False
            collector.is_real = False
            collector.save()
        else:
            areas = Areas.objects.all()

            context = {
                    'areas': areas,
                    'message': 'password does not match',
            }
            return render(request, 'register.html',context) 
        return render(request, 'waiting.html')
    # elif request.method == 'GET':
    #     collector = Collector.objects.all()
    #     collector_serializer = Collectorserializer(collector, many =True)
    #     return JsonResponse(collector_serializer.data, safe=False)
    # elif request.method == 'PUT':
    #     collector_data = JSONParser.parse(request)
    #     collector = Collector.objects.get(Username=collector_data['username'])
    #     collector_serializer = Collectorserializer(collector, data=collector_data)
    #     if collector_serializer.is_valid():
    #         collector_serializer.save()
    #         return JsonResponse("updated Successfully" , safe=False)
    #     return JsonResponse("Couldn't update" , safe=False)
    # elif request.method == 'DELETE':
    #     collector = Collector.objects.get(username = User.username)
    #     collector.delete()
    #     return JsonResponse("deleted Successfully" , safe=False)
    




registerKey = True


def loginn(request):

    # registerKey = True
    global registerKey
    registerKey = True

    context ={
        'registerKey': registerKey
    }

    return render(request, 'login.html', context)

def login_req(request):
    if request.method == 'POST':
    #    print ("session 2 ")
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            return render(request,'login.html',{'message':'PLEASE ENTER CORRECT USERNAME'})
        collector = Collector.objects.get(user = user)
        houses = Houses.objects.filter(area = collector.area)
        authenUser = authenticate(username = username, password = password)
        if authenUser is not None:
            if collector.is_real == True:
                login(request, authenUser)

            if collector.is_admin == True:
                context = {
                    'adminKey': True,
                    'collector': collector,
                    'house': houses,
                    'user':user,

                }
                # return render(request, 'admin-panel.html',context)
                return redirect('admin-panel')
            elif collector.is_real == True:
                context = {
                    'adminKey': True,
                    'memberkey': True,
                    'collector': collector,
                    'houses': houses,
                    'user':user,

                }
                return render(request, 'member-panel.html', context)
            else:
                context = {
                    'registerKey':registerKey,
                    'message':'YOUR ACCOUNT IS NOT ACTIVATED !'
                }
                return render(request,'login.html', context)
        else:
            context = {
                'registerKey':registerKey,
                'message':'PLEASE LOGIN WITH A CORRECT PASSWORD',
            }
            return render(request,'login.html',context)
    else:
        context = {
            'registerKey':registerKey,
            # 'message': 'There was a problem login'
        }
        return render(request, 'login.html', context)


# @login_required(login_url='login-req')
def login_output(request):
    user = User.objects.all()
    if request.user in user:
        # print('session 1')
        collector = Collector.objects.get(user = request.user)
        # print("hi this is a user:", collector.is_real)
        houses = Houses.objects.filter(area = collector.area)
        if collector.is_admin == True:
            # print('this is a admin ')
            context ={
                'adminKey': True,
                'collector': collector,
                'house': houses,
                'user':user,
            }
            return render(request,'admin-panel.html', context)
        elif collector.is_real == True:
            # print('this is collector')
            context = {
                'adminKey': True,
                'memberkey': True,
                'collector': collector,
                'houses': houses,
                'user':user,
            }
            return render(request, 'member-panel.html', context)
        else:
            # print("not authenticated")
            context = {
                        'registerKey':registerKey,
                        'message':'YOUR ACCOUNT IS NOT ACTIVATED !'
                    }
            
            return redirect('login-req')
    else:
        pass 

# @login_required(login_url='login-output')
def admin_panel(request):
    collector = Collector.objects.get(user = request.user)
    houses = Houses.objects.filter(area = collector.area)
    context ={
        'collector': request.user.username,
        'adminKey': True,
        'collector': collector,
        'house': houses,
        'user': request.user,
    }
    return render(request, 'admin-panel.html', context)

# @login_required(login_url='login-output')
def admin_profile(request):
    user = User.objects.get(username=request.user.username)
    profile = Collector.objects.get(user=user)
    adminKey = True
    context = {
        'profile': profile,
        'adminKey': adminKey,
    }
    return render(request, 'adminprofile.html', context)

def reset(request):
    houses_chk = Houses.objects.all()
    collectors =Collector.objects.all()
    for i in collectors:
        i.area_status = False
        i.save()
    for i in houses_chk:
        print(i.is_completed,type(i.is_completed))
        i.is_completed = 'Not Completed'
        i.collector = None
        i.save()
        print("Status changed to false")
    return redirect('viewarea')

# @login_required(login_url='login-output')
def member_job_status(request):
    global findKey
    findKey = True

    if request.method == 'GET':

        # username = request.user.username

        houses_checked = request.POST.getlist('houses')
        user = User.objects.get(username='soya')
        print(user)
        collector = Collector.objects.get(user = user)
        print(collector)
        houses = Houses.objects.filter(area=collector.area)
        print("list of checked houses: ",houses_checked,"Q:->",houses,"Name:",collector,"time :",datetime.now(),len(houses))
        for i in range(len(houses)):
            print("Inside for loop",i+1,houses_checked)
            if str(i+1) in houses_checked:
                print("Inside if block")
                houses[i].is_completed = "Completed"
                houses[i].collector = collector
                houses[i].save()
                print(houses[i].is_completed, houses[i].collector, houses[i])
                data.append([collector,houses[i].house_name,datetime.now()])
            print("After for loop",i)
        context ={
                'collector': collector,
                'houses': houses,
                'adminKey': True,
                'memberkey': True,
                }
        return render(request, 'member-panel.html', context)
    else:
        
        collector = Collector.objects.get(user=request.user)
        houses = Houses.objects.filter(area=collector.area)
        context ={
                'collector': collector,
                'houses': houses,
                'adminKey': True,
                }
        return render(request, 'member-panel.html', context)

# @login_required(login_url='login-output')
def admin_permissions(request):
    areas = Areas.objects.all()
    #collectors = Collector.objects.prefetch_related('area', 'user').all()
    collectors = Collector.objects.all()
    collector_houses = {}
    for collector in collectors:
            # print(" .........entered if ............")
            # print(collector.area.area_name)
            houses = Houses.objects.filter(area = collector.area.id)
            collector_houses[collector] = houses
            for house in houses:
                pass
                # print("Name:", collector.user.username)
                # print("houses: ",house.house_name)
                # print("address: ",house.house_address)
    # print("collectors: ", collectors)
    adminKey = True
    findKey = True

    context = {
        'collectors': collectors,
         'adminKey': adminKey,
         'findKey': findKey,
         'houses': houses,
         'collector_houses' : collector_houses,
         'downloadKey': True,
    }

    return render(request, 'admin-permissions.html', context)

# @login_required(login_url='login-output')
def admin_permissions_save(request, username):

    if request.method == 'POST':

        adminChoice = request.POST.get('admin')

        user = User.objects.get(username = username)

        # print(user.username)

        if adminChoice == "True":
            adminChoice = True
        else: 
            adminChoice = False

        Collector.objects.filter(user = user).update(is_admin = adminChoice)

    return redirect('admin-permissions')

# @login_required(login_url='login-output')
def collector_authentic_permissions(request, username):

    if request.method == 'POST':

        isRealChoice = request.POST.get('real')

        if isRealChoice == "True":
            isRealChoice = True
        else: 
            isRealChoice = False

        user = User.objects.get(username = username)
        Collector.objects.filter(user=user).update(is_real = isRealChoice)

    return redirect('admin-permissions')

# @login_required(login_url='login-output')
def admin_area(request):

    adminKey = True
    areas = Areas.objects.all()

    if request.method == 'POST':

        area_name = request.POST.get('areaname')
        house_name = request.POST.get('housename')
        address = request.POST.get('address')
        house = Houses()

        if (Areas.objects.filter(area_name=area_name).exists()):
            # print ('Areas already exists')
            house.area = Areas.objects.get(area_name=area_name)
            house.house_name = house_name
            house.house_address = address
            house.save()
        else:
            # print("areas not exists")
            area = Areas()
            area.area_name = area_name
            area.save()
            # areas = Areas.objects.get(area_name = request.POST.get('area'))  
            # print('Area is added now !')
            house.area = area
            house.house_name = house_name
            house.house_address = address
            house.save()
        context ={
            'adminKey' : adminKey,
            'areas': areas,
            'success' : "your response has been recorded",
        }
        return render(request, 'adminarea.html', context)
    else:
        context = {
            'adminKey' : adminKey,
            'areas': areas,
        }

        return render(request, 'adminarea.html', context)

# @login_required(login_url='login-output')
def viewarea(request):
    adminKey = True

    area = Areas.objects.all()
    # print("hi ther:", id)
    houses = Houses.objects.all()
    
    # print("areas are: ", area)
    # print("houses: ", houses)
    context = {
        'adminKey' : adminKey,
        'houses': houses,
        'areas': area,
        'viewarea': True,
    }
    return render(request, 'viewareas.html', context)

@login_required(login_url='login-output')
def admin_search(request):
    adminKey = True
    if request.method == 'POST':

        findout = request.POST['username']
        user = User.objects.filter(username__contains = findout)
        search = list(Collector.objects.filter(user_id__in = user))
        area = Areas.objects.filter(area_name__contains = findout)
        # print("area: ",area)
        search += set(list(Collector.objects.filter(area_id__in= area)))
        search = list(search)
        # print("this is the area: " ,search)

        collector_houses = {}
        for collector in search:
            houses =Houses.objects.filter(area_id = collector.area_id )
            collector_houses[collector] = houses
            
            # print ('search is here:', search)
        context = {
            'search' : search,
            'adminKey' : adminKey,
            'collector_houses': collector_houses,
            'findKey': True,
        }

        return render(request, 'admin-search.html',context)
    else:
        return HttpResponse("not found", status=404)

def logoutt(request):
    logout(request)
    #return render(request,'home.html')
    return redirect('/')