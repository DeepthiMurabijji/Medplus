ch=int(input(" 1:Parking \n 2:Deallocation \n 3:Exit \n Enter your Choices: "))
while(ch==1 or ch==2 or ch==3):
    if(ch==1):
        name='bike'             #input("Enter type of vehicle: ")
        Milage=40                  #   int(input("Enter the milage of the vehicle: "))
        capacity=2                 #int(input("Enter the capacity of the vehicle: "))
        width= 5            # int(input("Enter the width of the vehicle: "))
        depth= 5          #int(input("Enter the depth of the vehicle: "))
        num='b2'              #input("Enter the vehicle Number: ")
        man= 'lol'                #input("Enter the vehicle Manufacture: ")
        intime= '9:00'           #input("Enter the InTime: ")

        space=width*depth

        parkingLotArea = 10 * 10

    dictionArea = {

        'A':{
            'car': parkingLotArea * 0.6,
            'bike': parkingLotArea * 0.03,
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
        'cars':{},
        'bus':{}
    }

    for keys, values in dictionArea.items():
        if space <= dictionArea[keys]['bike']:
            dictionArea[keys]['bike'] -= space
            print(dictionArea[keys]['bike'])
            temp=vehicle['bike']
            temp[num]=[keys,space,intime]
            print('Vehicle Number: ',num)
            print(temp[num])
            #print(keys)
            break
    #print(" i am here")
    if ch==2:
        #print("I am inside")
        k='b2'
        veh=""
        for i in vehicle:
            #print(i,vehicle[i])
            if k in vehicle[i]:
                temp1=vehicle[i]
                temp=temp1[k]
                L=temp[0]
                Area=temp[1]
                T=temp[2]
                del temp
        # for keys, values in dictionArea.items():
        #     print(veh,keys)
        #     dictionArea[keys][veh] += Area
                tempo=dictionArea[L]
                tempo[i]+=Area
                print("Space is Delocated.")
                break

    if(ch==3):
        exit(0)
    ch=int(input(" 1:Parking \n 2:Deallocation \n 3:Exit \n Enter your Choices: "))


        

        
