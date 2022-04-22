import csv 
from datetime import time 
from fileinput import filename

with open('Employee_details.csv','w') as file:
    header= ['ID','emp_Name','dept','login','logout','Breakfrm','BreakTo']
    play=csv.DictWriter(file,fieldnames=header)
    play.writeheader()
    play.writerow({'ID':1,'emp_Name':'John Smith','dept':'Account','login':'10:30','logout':'19:30','Breakfrm':'13:00','BreakTo':'14:00'})
    play.writerow({'ID':2,'emp_Name':'Erica Meyers','dept':'IT','login':'9:30','logout':'18:30','Breakfrm':'12:00','BreakTo':'13:00'})
    play.writerow({'ID':3,'emp_Name':'Nil Mills','dept':'Account','login':'11:30','logout':'20:30','Breakfrm':'14:00','BreakTo':'15:00'})





