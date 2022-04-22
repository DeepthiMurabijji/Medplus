class vehicle:
    def __init__(self, name, number, manufacturer, inTime):
        self.name = name
        self.number = number
        self.manufacturer = manufacturer
        self.inTime = inTime
        self.lot = None


class bus(vehicle):
    def __init__(self, milage, name, width, depth, number, manufacturer, inTime, capacity=45):
        self.milage = milage
        self.width = width
        self.depth = depth
        self.capacity = capacity
        vehicle.__init__(self, name, number, manufacturer, inTime)


class car(vehicle):
    def __init__(self, milage, name, width, depth, number, manufacturer, inTime, capacity=4):
        self.milage = milage
        self.width = width
        self.depth = depth
        self.capacity = capacity
        vehicle.__init__(self, name, number, manufacturer, inTime)


class bike(vehicle):
    def __init__(self, milage, name, width, depth, number, manufacturer, inTime, capacity=2):
        self.milage = milage
        self.width = width
        self.depth = depth
        self.capacity = capacity
        vehicle.__init__(self, name, number, manufacturer, inTime)


class Lot:
    def __init__(self, width, depth, series, number=0):
        self.width = width
        self.depth = depth
        self.number = number
        self.series = series
        self.bikeArea = 0.3*(self.width*self.depth)
        self.carArea = 0.6*(self.width*self.depth)
        self.busArea = 0.1*(self.width*self.depth)

    def getter_bikeArea(self):
        return self.bikeArea

    def setter_bikeArea(self, diffArea):
        self.bikeArea += diffArea

    def getter_carArea(self):
        return self.carArea

    def setter_carArea(self, diffArea):
        self.carArea += diffArea

    def getter_busArea(self):
        return self.busArea

    def setter_busArea(self, diffArea):
        self.busArea += diffArea


class subLot:
    def __init__(self, number, vehicleNum, status="Free"):
        self.number = number
        self.status = status
        self.vehicleNum = vehicleNum


def newLot(Lseries):
    global Lots, ser
    print("Create a New Lot : ")
    print("The New Lot Created is : ", ser[Lseries])
    print("Enter Width and Depth of the Slot", ser[Lseries])
    width, depth = map(int, input().split())
    obj = Lot(width, depth, ser[Lseries])
    Lots[obj] = []

def parkingLot(type, vehicle):
    global Lots, lotsAllocated, Lnumber, ser, Lseries
    pass


def delocationLot(number, outTime):
    global Vehicles,Lots
    for i in Vehicles:
        if number in Vehicles[i]:
            temp=Vehicles[i]
            obj = temp[number].lot
            for j in Lots:
                temp1=Lots[j]
                if obj in temp1:
                    print("Your Vehicle is at Slot : ",str(j.series)+str(obj.number))
            set = getattr(j, str("setter_"+str(i.lower())+"Area"))
            var=(temp[number].width*temp[number].depth)
            set(var)
            print(j.getter_bikeArea(),var)
            print("The Charge is : ",cost(number,outTime))
            obj.status="Free"
            obj.vehicleNum="____"
            del temp[number]
    



def tim_min(s):
    i = s.split(':')
    mins = int(i[0])*60+int(i[1])
    return mins


def cost(num,outTime):
    veh = None
    for i in Vehicles:
        if num in Vehicles[i]:
            temp = Vehicles[i]
            veh = temp[num]
    diff=tim_min(outTime)-tim_min(veh.inTime)
    c=0
    if diff>30:
        c+=20
        diff-=60
        if diff>0:
            n=diff//60
            if n>9:
                c=c+(9*10)+(n-9)*5
                if diff%60>30:
                    c=c+5
            c=c+n*10
            if diff%60>30:
                c=c+10
    return c


Vehicles = {'Bus': {}, 'Car': {}, 'Bike': {}}
Lots = {}
parkedVehicles = {}
Lnumber = 1


ser = 'ABCD'
Lseries = 0
ch = input("\n 1.Parking Lot \n 2.Deallocating Lot \n Press anyother key to terminate the process.\n Enter Your Choice : ")
if ch == '1':
    newLot(Lseries)
    Lseries+=1


while(ch == '1' or ch == '2'):
    if ch == '1':
        print("Enter your vehicle details : ")
        inTime = input("Enter your inTime in 24hrs Format : ")
        milage = input("Enter milage of your Vehicle : ")
        name = input("Enter your Vehicle Type (Bus/Car/Bike): ").lower()
        width = int(input("Enter Width of your Vehicle : "))
        depth = int(input("Enter Depth of your Vehicle : "))
        capacity = int(input("Enter Capacity of your Vehicle : "))
        number = input("Enter your vehicle number : ")
        manufacturer = input("Enter the manufacturer : ")
        x = name.capitalize()
        temp = Vehicles[x]
        temp[number] = eval(name)(milage, name, width, depth, number, manufacturer, inTime,capacity)
        for k in range(len(Lots)):
            pk=[]
            for i in Lots:
                pk.append(i)
            i=pk[k]
            tempMethod = getattr(i, str("getter_"+str(x.lower())+"Area"))
            if  int(tempMethod()) >= (width*depth):
                set = getattr(i, str("setter_"+str(x.lower())+"Area"))
                var=-1*(width*depth)
                set(var)
                if len(Lots[i])==0:
                    Numb = i.number
                    i.number = Numb+1
                    newSub = subLot(Numb+1, number, "Occupied")
                    Lots[i].append(newSub)
                    temp[number].lot=newSub
                else:
                    for j in Lots[i]:
                        if j.status == "Free":
                            j.status="Occupied"
                            j.vehicleNum=number
                            temp[number].lot=j
                            break
                    else:
                        Numb = i.number
                        i.number = Numb+1
                        newSub = subLot(Numb+1, number, "Occupied")
                        Lots[i].append(newSub)
                        temp[number].lot=newSub
                break
        else:
            if Lseries==4:
                print("The Lot Places for",x,"are filled and are currently unavailable.")
                print()
            else:
                newLot(Lseries)
                Lseries+=1

    if ch=='2':
        num=input("Enter your Vehicle Number : ")
        outTime=input("Enter the Present time in 24hrs Format : ")
        delocationLot(num,outTime)
    for i in Lots:
        M=getattr(i, str("getter_"+str(x.lower())+"Area"))
        print("The Lot Name:",i.series,"\nNumber of Sub Lots :",str(i.number),"\nRemaining Area for",str(x)+":"+str(M()))
        temp=Lots[i]
        for j in temp:
            print(j.number,j.vehicleNum,j.status)

    ch = input("\n 1.Parking Lot \n 2.Deallocating Lot \n Press anyother key to terminate the process.\n Enter Your Choice : ")