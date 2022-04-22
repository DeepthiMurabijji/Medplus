import csv 
from datetime import datetime
from email import header
from csv import DictReader
from fileinput import filename



with open('Employee_details.csv',newline='')as file:
    read=DictReader(file)

    id=[]
    name=[]
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
        name.append(i['emp_Name'])

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

    inteStr = inte.split(".")
    inteFirst = int(inteStr[0])
    inteSecond = int(inteStr[1])
    inteTotal = inteFirst * 60 + inteSecond/100 * 60

    #print(inteTotal)
    return (inteTotal)

def minutesToHours(inte):
    varMin = (inte % 60)/60
    varHours = inte//60
    varTotal = varMin + varHours

    return varTotal

employeeTableMinutes = []

for x in emp:

    temp = []
    for y in x:
       temp.append(hrToMinString(y))

    employeeTableMinutes.append(temp)


#print(employeeTableMinutes)
'''
employeeTableMinutes = [
    [618.0, 780.0, 840.0, 1158.0], 
    [558.0, 720.0, 780.0, 1098.0], 
    [678.0, 840.0, 900.0, 1218.0]
]
'''

breakList = []
inOutList = []
for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(4):
        if(y==0 or y==3):
            temp.append(employeeTableMinutes[x][y])

    inOutList.append(temp)

#print(inOutList)

for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(1, len(employeeTableMinutes[0])-1):
        temp.append(employeeTableMinutes[x][y])

    breakList.append(temp)

#print(breakList)


emp = []

for x in range(len(inOutList)):
    temp = []
    for y in range(1):
        temp1 = []
        temp2 = []
        temp1.append(inOutList[x][y])
        temp2.append(inOutList[x][y+1])
    temp.append(temp1)
    temp.append(breakList[x])
    temp.append(temp2)
    emp.append(temp)
# print("The meeting timeline Intial:")
# print(emp)

print("The Employee Details: ")
for i in range(len(id)):
    print(id[i],name[i])
print("--------------------------")
    

FIXME: TODO:

while (True):
    
    try:
       
        l= list(map(int,input("To whom do you want to schedule the meeting from the above list: ").split()))
        
    except:
        print("Please enter valid Emplyoee ID Next Time.")
        exit(0)
        
    try:
        duration=input("Enter the duration of the meeting in only (H% : M%)format : ")
        duration = hrToMinString(duration)
    

    except ValueError:
        print("please enter the time in correct format! In Futher.")
        print("---- Format is hours:minutes eg:(1:00)for 1hour ---- ")
        exit(0)
        # duration=input("Enter the duration of the meeting in only (H% : M%)format : ")
        # duration = hrToMinString(duration)
    
    



    
    outMax = []
    inMax=[]
    for d in inOutList:
        inMax.append(d[0])
    maxintime=max(inMax)
        #print(inMax)
        #print(a)
    for x in inOutList:
        outMax.append(x[1])
    maxouttime = max(outMax)




    while (True):
 
        count=0
        for i in range(len(l)):
            for j in range(len(emp[i])-1):
                if(j==0):
                    if(emp[i][j][0] <= maxintime and emp[i][j+1][0] >= maxintime + duration):
                        count+=1
                else:
                    if(emp[i][j][1] <= maxintime and emp[i][j+1][0] >= maxintime + duration):
                        count+=1
        
        c=0
        if(count == len(l)):
            for i in range(len(l)):
                temp=[]
                for j in range(1):
                    temp.append(maxintime)
                    temp.append(maxintime+duration)
                
                emp[i].append(temp)
                emp[i].sort()

                start=  minutesToHours(temp[0])                     #maxintime
                end=  minutesToHours(temp[1])              #maxintime+duration

                if(c==0):
                    print("Your Meeting is scheduled from {} to {} ".format(minutesToHours(temp[0]), minutesToHours(temp[1])))
                    print()

                c+=1
            break
        else:
            maxintime += duration
        
        if(maxintime >= maxouttime):
            print("Meeting Not Possible!!!")
            break
    
    header = ["Employee ID's", 'Start Time', 'End Time' ]
    data = [l,start,end]
    filename = 'Meeting Arranged.csv'
    with open(filename, 'a',newline='') as file:
        csvwrite = csv.writer(file)
        csvwrite.writerow(header)
        csvwrite.writerow(data)



    print()
    ch=input("Do you want any other Meeting to be scheduled[y/n]: ")
    if(ch=='y'):
        pass
    else:
        print("Thank you!!!")
        exit(0)














        
       



