'''
input = [1,2,3]

result = [2* x for x in input]
print(len(result))
print(result)


def is_even(x):
    return x%2 == 0

def square(x):
    return x*x
#result = [square(x) for x in input]
result = [square(x) for x in range(5) if is_even(x)]
print(result)


words = ["one\n", "two\n", " three\n"]
result = [word.strip() for word in words]
print(result)


result = [(x+y) for x in range(3) for y in range(3)]
result = [(x+y) for x in range(3) for y in range(3) if is_even(x+y)]


result = { i : chr(65 +i) for i in range(4)}

result = { v: k for k,v in result.iteritems()}


import string 
result = { x : ord(x)-ord('A') + 1 for x in string.uppercase[:5] }


result = { x**2 for x in range (5) if x % 2 == 1}
print(len(result))
print(result)


all = set(range(10))
evens = {x for x in all if x%2 == 0}
print(evens)



import inspect
import symtable
count = 10
def get_global_count():
    return count

def test_scope_basic():
    local_names = get_locals(test_scope_basic)

    value = count
    print('value' in local_names)
    print('value' in global_names)
    x=('count' in global_names)
    print(x)
    


def test_classes_are_object_factories():
    class Queue(object):
        pass

    q1 = Queue()  # you can 'call' a class to create an instance
    q2 = Queue()
    
    print(type(q1).__class__)
    
  
def test_classes_bound_and_unbound_methods():
    class Queue(object):
        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            self._queue.append(obj)

        def pop(self):
            return self._queue.pop(0)

    q1 = Queue("q1")
    q1_push = q1.push
    print (q1.push)
    #print (Queue.push)

   

from datetime import datetime
import time 
x='7:00PM'
f='%I:%M%p'
d=datetime.strptime(x,f)
print(d)

y='10:00AM'
c=datetime.strptime(y,f)
z=d-c
print(z)

from re import M
from tkinter import N


s={
    'A':{1:1500, 2:3000, 3:500}, 
    'B':{1:1500, 2:3000, 3:500}, 
    'c':{1:1500, 2:3000, 3:500}, 
    'D':{1:1500, 2:3000, 3:500} 
}
num='apv123'
rm=1500

for i in s:
    if(rm != s[i][1]):
        print(rm,s[i][1])
        print("bike parked")
        print(num ,i )
        print()
        break

        
from turtle import width
from numpy import append, arange


class Vehicle:
    def details(self,name,milage,capacity,width,depth,num,man,intime):
        pass
        
class Bike(Vehicle):
    def details(self, name, milage, capacity, width, depth, num, man,intime):
        return super().details(name, milage, capacity, width, depth, num, man,intime)
class Car(Vehicle):
    def details(self, name, milage, capacity, width, depth, num, man,intime):
        return super().details(name, milage, capacity, width, depth, num, man,intime)
class Bus(Vehicle):
    def details(self, name, milage, capacity, width, depth, num, man,intime):
        return super().details(name, milage, capacity, width, depth, num, man,intime)


class ParkingLot(Vehicle):
    def parkingdetails(self):
        self.totalarea=5000
        self.bikeparkingarea=1500
        self.carparkingarea=3000
        self.busparkingarea=500


class Parkingseries(ParkingLot):
# series A Starts.......
    def A (self,rm,space,name,bikeparkingarea,carparkingarea,busparkingarea):
        if(name=='bike'and space <= bikeparkingarea):
            bikeparkingarea = bikeparkingarea - space
            rm = bikeparkingarea

            return rm
        elif(name=='car' and space <= carparkingarea):
            carparkingarea = carparkingarea - space
            rm = carparkingarea
            return rm
        elif(name=='bus' and space <= busparkingarea ):
            busparkingarea = busparkingarea - space
            rm = busparkingarea
            return rm
        else:
            v.B(rm,space,name)
        

# series B......
    def B(self,rm,space,name,totalarea,bikeparkingarea,carparkingarea,busparkingarea):
        if(name=='bike' and space <= bikeparkingarea):
            bikeparkingarea = bikeparkingarea - space
            rm = bikeparkingarea
            return rm
        elif(name=='car' and space <= carparkingarea):
            carparkingarea = carparkingarea - space
            rm = carparkingarea
            return rm
        elif(name=='bus' and space <= busparkingarea):
            busparkingarea = busparkingarea - space
            rm = busparkingarea
            return rm
        else:
            v.C(rm,space,name)

# Series C ......    

    def C(self,rm,space,name,bikeparkingarea,carparkingarea,busparkingarea):
        if(name=='bike'and space <= bikeparkingarea):
            bikeparkingarea = bikeparkingarea - space
            rm = bikeparkingarea

            return rm
        elif(name=='car' and space <= carparkingarea):
            carparkingarea = carparkingarea - space
            rm = carparkingarea
            return rm
        elif(name=='bus' and space <= busparkingarea):
            busparkingarea = busparkingarea - space
            rm = busparkingarea
            return rm
        else:
            v.D(rm,space,name)

# Series D .......
    def D(self,rm,space,name,totalarea,bikeparkingarea,carparkingarea,busparkingarea):
        if(name=='bike' and space <= bikeparkingarea):
            rm = bikeparkingarea - space
            return rm
        elif(name=='car'):
            rm = carparkingarea - space
            return rm
        elif(name=='bus'):
            rm = busparkingarea - space
            return rm
        else:
            print("OOP's! There is no parking space...")

   

    

ch=int(input(" 1:Parking \n 2:Deallocation \n 3:Exit \n Enter your Choices: "))  
parkedbike=[]
parkedcar=[]
parkedbus=[]
barea=[]
carea=[]
busarea=[]
rm=0
s={'A':{'a1':1500, 'a2':3000, 'a3':500}, 
'B':{'b1':1500, 'b2':3000, 'b3':500}, 
'c':{'c1':1500, 'c2':3000, 'c3':500}, 
'D':{'d1':1500, 'd2':3000, 'd3':500} }
series=['A','B','C','D']
if (ch==1):
    name=input("Enter type of vehicle: ")
    Milage=int(input("Enter the milage of the vehicle: "))
    capacity=int(input("Enter the capacity of the vehicle: "))
    width=int(input("Enter the width of the vehicle: "))
    depth=int(input("Enter the depth of the vehicle: "))
    num=input("Enter the vehicle Number: ")
    man=input("Enter the vehicle Manufacture: ")
    intime=input("Enter the InTime: ")

    v=Vehicle()
    

    space=width*depth
    v.details(name,Milage,capacity,width,depth,num,man,intime)

'''


