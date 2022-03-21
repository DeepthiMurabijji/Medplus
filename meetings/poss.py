import csv 
from datetime import datetime
from email import header
from csv import DictReader

with open('Employee_details.csv',newline='')as file:
    read=DictReader(file)

    id=[]
    tim=[]
    emp=[]
    brk=[]
    #print(read)
    for i in read:
        #print(id)
        id.append(i['ID'])
        tim.append([i['login'],i['logout']])
        emp.append( [  i['login'] , i['Breakfrm'] ,i['BreakTo'] ,  i['logout']  ] )
        brk.append([i['Breakfrm'],i['BreakTo']])

# for i in range(len(emp)):
#     print(i,emp[i])
# print(id)
def hrToMinString(str):

    strSplit = str.split(":")
    hours = int(strSplit[0])
    minutes = int(strSplit[1])

    retMinutes = hours * 60 + minutes

    return int(retMinutes)


def hrToMinInteger(inte):

    inteStr = inte.split(":")
    inteFirst = int(inteStr[0])
    inteSecond = int(inteStr[1])
    inteTotal = inteFirst * 60 + inteSecond/100 * 60

    #print(inteTotal)
    return (inteTotal)

employeeTableMinutes = []

for x in emp:

    temp = []
    for y in x:
       temp.append(hrToMinInteger(y))

    employeeTableMinutes.append(temp)


print(employeeTableMinutes)
# mm=[]
# for i in range(len(employeeTableMinutes)):
#     mm.append(employeeTableMinutes[i][0])
# print(mm)
# print(max(mm))

'''
emp=[
    [[618], [60, 120], [438]], 
    [[558], [720, 60], [378]], 
    [[678], [120, 180], [498]]
]

n=[0,1,2]
duration=60
maximum = 0


for x in n:
    for y in range(len(emp[0]) - 1 ):
        if y == 0:
            diff = abs(emp[x][y][0] - emp[x][y+1][0])
            if diff > duration:
                if emp[x][y][0] >= maximum:
                    maximum = emp[x][y][0]
                    break
                
        else:
            diff = abs(emp[x][y][1] - emp[x][y+1][0])
            if diff > duration:
                if emp[x][y][1] >= maximum:
                    maximum = emp[x][y][1]
                    break

        #y += 1

temp = []


for i in n:
    temp.append(maximum)
    temp.append(int(maximum) + int(duration))
    emp[i].append(temp)
    emp[i].sort()
    

for i in range(len(emp)):
    print(emp[i])
    print()



print(maximum)

'''


while (True):
    l= list(map(int,input("Meeting For: ").split()))
    duration=int(input("Enter the duration of the meeting: "))

    duration = hrToMinInteger(duration)
    




    ch=input("Any Meeting to be scheduled[y/n]: ")
    if(ch=='y'):
        pass
    else:
        exit(0)














        
       



