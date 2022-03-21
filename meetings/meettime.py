
import csv 
from datetime import datetime
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
    reader = csv.reader(file)

    data =[]
    for i in reader:
        data.append(i)


def convert(li):
    f='%I:%M%p'
    x=datetime.strptime(li,f)
    return x


emp={}
a={}
b={}
lid=''

for i in range(len(data)):
    if (i== 0):
        continue
    id = data[i][0]
    login = data[i][3]
    logout = data[i][4]
    brk = [data[i][5],data[i][6]]
    emp[id] = [(login,brk[0]),(brk[1],logout)]
   
    
    for i in emp:
        
        pp=[]
        for m in range(2):
            k=[]
            for n in range(2):
                t=0
                li=emp[i][m][n]
                k.append(convert(li))
            pp.append(list(k))
        a[i]=[pp[0]]
        b[i]=[pp[1]]





        

#l= list(map(str,input("Meeting for: ").strip().split()))

for i in emp:
    for j in range(2):
        for k in range(2):
            print(emp[i][j][k])
            break

                   





