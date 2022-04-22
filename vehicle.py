from calendar import c
import csv
from fileinput import filename
from logging import exception

# fa = open('Allo.csv', 'w')
# writer = csv.writer(fa)
# header = ['vehicle Number','Type of vehicle','Block','InTime']
# writer.writerow(header)

# fd = open('Dello.csv', 'w')
# writer1 = csv.writer(fd)
# header = ['vehicle Number','Type of vehicle','Block','InTime','Out Time','Cost']
# writer1.writerow(header)

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

parkingLotArea = 10 * 10
dictionArea = {
    'A':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    },
    'B':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    },
    'C':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    },
    'D':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    }
}

vehicle={
    'bike':{},
    'car':{},
    'bus':{}
}


def docu1(num,name,keys,intime):
    header = ['vehicle Number','Type of vehicle','Block','InTime']
    data=[(num),(name),(keys),(intime)]
    filename = 'Allocation.csv'
    with open(filename,'a+',newline="") as file:
        csvwrite = csv.writer(file)
        csvwrite.writerow(header)
        csvwrite.writerow(data)



def allocation():
    global dictionArea,vehicle
    name= input("Enter type of vehicle: ")
    try:
        if(name=='bike' or name=='car' or name=='bus' ):
            pass
        else:
            raise ValueError
    except ValueError :
        print("please enter the valid type (i.e bike/car/bus)only!! ")
        exit(0)
            
            
    Milage= 40    #int(input("Enter the milage of the vehicle: "))
    capacity= 2 # int(input("Enter the capacity of the vehicle: "))
    if (name=='bike'):
        print("Please enter the Area of the bike less or equal to 30(i.e L*b<=30)")
    elif(name=='car'):
        print("Please enter the Area of the bike less or equal to 60(i.e L*b<=60)")
    elif(name=='bus'):
        print("Please enter the Area of the bike less or equal to 60(i.e L*b<=60)")

        
    try:
    
        width= int(input("Enter the width of the vehicle: "))
        depth= int(input("Enter the depth of the vehicle: "))
    except:
        print("enter the width and depth in number and in specified area!!!")
        exit(0)

    num= input("Enter the vehicle Number: ")
    man=  'lorf' #input("Enter the vehicle Manufacture: ")
    intime= '9:00' #input("Enter the InTime: ")
    space=width*depth

    for keys, values in dictionArea.items():
        if space <= dictionArea[keys][name]:
            dictionArea[keys][name] -= space
            print("Remaining Area in the block: ",dictionArea[keys][name])
            temp=vehicle[name]
            temp[num]=[keys,space,intime]
            print('Vehicle Number: ',num)
            print(temp[num])
            #writer.writerow([num,name,keys,intime])
            docu1(num,name,keys,intime)
            return True
    return False

def costcal(inTime,outTime):
    it=list(map(int,inTime.split(':')))
    it=it[0]*60+it[1]
    ot=list(map(int,outTime.split(':')))
    ot=ot[0]*60+ot[1]
    duration = abs(ot - it)
    c=0
    if (duration > 30):
        c+=20
        duration-=60
        count=0
        while(duration > 30 and count < 10):
            count+=1
            c+=10
            duration-=60
            while(duration > 30):
                c+=5
                duration-=60
    if c==0:
        print("No need to pay! cost is: ",c)
    else:
        print("Amount to be paid for parking: ",c)
    return c
    
  

def deallow(num,name,keys,intime,ot,cost):
    header = ['vehicle Number','Type of vehicle','Block','InTime','OutTime','Cost']
    #writer1.writerow([num,name,keys,intime,ot,cost])
    data=[num,name,keys,intime,ot,cost]
    filename = 'Deallocation.csv'
    with open(filename,'a',newline="") as file:
        csvwrite = csv.writer(file)
        csvwrite.writerow(header)
        csvwrite.writerow(data)
   

def Deallocation():
    global dictionArea, vehicle
    k=input("enter your vehicle number: ")
    try:
        OT=input("enter the logout time in (hours:minutes)format only: ")
    except:
        print("Please enter the correct format of the time")
        print("---- Format is hours:minutes eg:(15:00)for 3PM ---- ")
    
    ot=OT
    for i in vehicle:
        #print(i,vehicle[i])
        if k in vehicle[i]:
            temp1=vehicle[i]
            temp=temp1[k]
            L=temp[0]
            Area=temp[1]
            T=temp[2]
            #print(temp,L,Area,T)
            c=costcal(T,ot)
            del temp
            tempo=dictionArea[L]
            tempo[i]+=Area
            print("Space is Delocated.")
            deallow(k,i,L,T,OT,c)
            return True
    return False

ch=int(input(" 1:Parking \n 2:Deallocation \n 3:Exit \n Enter your Choices: "))
print("-------------------------------------")
while(ch==1 or ch==2 or ch==3):
    if(ch==1):
        if allocation():
            print("vehicle is parked!")
            
        else:
            print("No parking space !!!")
            print("width and depth of the vehicle exceeds!!!")
    if(ch==2):
        if Deallocation():
            print("Your Vehicle is Deallocated!")
        else:
            print("Error!! in Deallocation.")
            print("There is No vehicle with that Name!!! \n>>Please try again")
    if(ch!=1 and ch!=2):
        print("THANK YOU FOR VISITING!!")
        exit(0)
    ch=int(input(" 1:Parking \n 2:Deallocation \n 3:Exit \n Enter your Choices: "))
    print("-------------------------------------")
    
#fa.close()
#fd.close
        


    


       

                








        


