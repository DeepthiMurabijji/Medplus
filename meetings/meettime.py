
import csv 
from datetime import datetime
from csv import DictReader
import time
'''
import pandas as pd
play= pd.read_csv('Employee_details.csv')

#play.info()
#print(play.values)
#print(play.shape)
#print(play.dtypes)
#print(play.head())
#print(play['dept'].value_counts())


with open('Employee_details.csv','r') as file:
    read = csv.reader(file)
    header = next(csv)




n=int(input("enter the number: "))
a=[input() for i in range (n)]

FMT = '%H:%M:%S'
tdelta = datetime.strptime('10:30:00', FMT) - datetime.strptime('07:30:00', FMT)
print(tdelta)
'''
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



def hrToMinString(str):

    strSplit = str.split(":")
    hours = int(strSplit[0])
    minutes = int(strSplit[1])

    retMinutes = hours * 60 + minutes

    return int(retMinutes)

tableofmin=[]

for i in emp:
    temp=[]
    for j in i:
        temp.append(hrToMinString(j))
    tableofmin.append(temp)

#print(tableofmin)

'''     
tableofmin= [ 
    [630, 780, 840, 1170], 
    [570, 720, 780, 1110], 
    [690, 840, 900, 1230]
]
'''   
st1=[]
for i in range (len(tableofmin)):
    st1.append(tableofmin[i][0])
    
print(st1)
inmax=max(st1)
                





