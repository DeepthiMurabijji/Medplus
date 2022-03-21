'''

import csv
from fileinput import filename
header = ['name','marks','grade']
data = [['Alex',80,'B'],['Brad',45,'C'],['Joey',89,'A'],['jinx',98,'O']]

filename = 'Students_Data.csv'
with open(filename,'w',newline="") as file:
    csvwrite = csv.writer(file)
    csvwrite.writerow(header)
    csvwrite.writerows(data)


import pandas as pd
header = ['name','marks','grade']
data = [['Alex',80,'B'],['Brad',45,'C'],['Joey',89,'A'],['jinx',98,'O']]
data = pd.DataFrame(data, columns=header)
data.to_csv('stu_data.csv',index=False)

'''
import pandas as pd
data = pd.read_csv("Students_Data.csv")
data 