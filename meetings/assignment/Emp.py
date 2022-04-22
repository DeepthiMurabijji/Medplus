import csv
from email import header

filename = "Emp.csv"
file1 = open("Emp.csv")
data = csv.reader(file1)
#header = next(file1)
csv_data = []
for i in data:
    csv_data.append(i)


def time_min(s):
    hrs = ""
    mins = ""
    flag = 0
    for i in s:
        if i == ' ':
            break
        if i == ':':
            flag = 1
            continue
        if flag == 0:
            hrs += i
        elif flag == 1:
            mins += i
    tim = (int(hrs)*60)+int(mins)
    if 'PM' in s:
        tim += 720
    return tim


def min_time(a, b):
    pos = [a, b]
    x = 0
    y = 0
    tl = ""
    if pos[0] > 779:
        x = ((pos[0]-720)//60)
        y = int(((pos[0]-720) /
                 60-(pos[0]-720)//60)*60)
        if y == 0:
            y = "00"
        print(x, ":", y, "pm", end=" to ")
        tl = "pm"
    else:
        x = (pos[0])//60
        y = int(((pos[0])/60 -
                (pos[0])//60)*60)
        if y == 0:
            y = "00"
        print(x, ":", y, "am", end=" to ")
        tl = "am"
    frm = str(x)+":"+str(y)+tl
    tl = ""
    if pos[1] > 779:
        x = (pos[1]-720)//60
        y = int(((pos[1]-720) /
                60-(pos[1]-720)//60)*60)
        if y == 0:
            y = "00"
        print(x, ":", y, "pm", end=" ")
        tl = "pm"
    else:
        x = (pos[1])//60
        y = int(((pos[1])/60 -
                (pos[1])//60)*60)
        if y == 0:
            y = "00"
        print(x, ":", y, "am", end=" ")
        tl = "am"
    To = str(x)+":"+str(y)+tl
    print()
    print()
    return frm, To


print()
Emp = {}
T1 = {}
T2 = {}
lid = ""

for i in range(len(csv_data)):
    if i == 0:
        continue
    x = csv_data[i][0]
    login = csv_data[i][1]
    logout = csv_data[i][2]
    brk = [csv_data[i][3], csv_data[i][4]]
    Emp[x] = [(login, brk[0]), (brk[1], logout)]
    #print(len(Emp))
    for i in Emp:
        Pp = []
        for m in range(2):
            k = []
            for n in range(2):
                tt = 0
                li = Emp[i][m][n]
                k.append(time_min(li))
            Pp.append(list(k))
        T1[i] = [Pp[0]]
        T2[i] = [Pp[1]]
        #print(T1[i], T2[i])


def check(l1, l2, s, hrs):
    num = -99999
    ind = 0
    for i in range(len(l1)):
        if num == 0:
            break
        if l1[i]-s >= 0 and l1[i]-s > num:
            ind = i
            num = l1[i]-s
    if s+hrs <= l2[ind]:
        return True
    return False


empFree = Emp
Meet = []
l = []


def schdMeet():
    print()
    global lid
    lid = input("Enter the Meeting Members' Employee IDs : ")
    l = list(map(str, lid .split()))
    print()
    hrs = input("Enter number of hours of the Meeting: ")
    hrs = int(float(hrs)*60)
    print()
    s1 = {}
    e1 = {}
    for i in l:
        s1[i] = []
        e1[i] = []
        for j in range(len(T1[i])):
            if T1[i][j][1]-T1[i][j][0] >= hrs:
                s1[i].append(T1[i][j][0])
                e1[i].append(T1[i][j][1])
    flag = 0
    m = 0
    for i in s1:
        if len(s1[i]) == 0 or len(e1[i]) == 0:
            flag = 1
            break
    if flag == 0:
        for i in s1:
            m = max(m, min(s1[i]))
    if flag == 0:
        for i in s1:
            if not check(s1[i], e1[i], m, hrs):
                flag = 1
    maxi1 = 0
    maxi2 = 0
    if flag == 0:
        m1 = m
        m2 = m+hrs
        for i in T1:
            j = 0
            while(j < len(T1[i])):
                if m1 in range(T1[i][j][0], T1[i][j][1]+1) and m2 in range(T1[i][j][0], T1[i][j][1]+1):
                    if T1[i][j][0] == m1 and T1[i][j][1] == m2:
                        del T1[i][j]
                    elif T1[i][j][0] == m1:
                        T1[i][j][0] = m2
                        j = j+1
                    elif T1[i][j][1] == m2:
                        T1[i][j][1] = m1
                        j = j+1
                    else:
                        T1[i].append([T1[i][j][0], m1])
                        T1[i].append([m2, T1[i][j][1]])
                        del T1[i][j]
                else:
                    j = j+1
        return m1, m2
    s1 = {}
    e1 = {}
    for i in l:
        s1[i] = []
        e1[i] = []
        for j in range(len(T2[i])):
            if T2[i][j][1]-T2[i][j][0] >= hrs:
                s1[i].append(T2[i][j][0])
                e1[i].append(T2[i][j][1])
    flag = 0
    m = 0
    for i in s1:
        if len(s1[i]) == 0 or len(e1[i]) == 0:
            flag = 1
            break
    if flag == 0:
        for i in s1:
            m = max(m, min(s1[i]))
    if flag == 0:
        if i in s1:
            if not check(s1[i], e1[i], m, hrs):
                flag = 1
    if flag == 0:
        m1 = m
        m2 = m+hrs
        for i in T2:
            j = 0
            while(j < len(T2[i])):
                if m1 in range(T2[i][j][0], T2[i][j][1]+1) and m2 in range(T2[i][j][0], T2[i][j][1]+1):
                    if T2[i][j][0] == m1 and T2[i][j][1] == m2:
                        del T2[i][j]
                    elif T2[i][j][0] == m1:
                        T2[i][j][0] = m2
                        j = j+1
                    elif T2[i][j][1] == m2:
                        T2[i][j][1] = m1
                        j = j+1
                    else:
                        T2[i].append([T2[i][j][0], m1])
                        T2[i].append([m2, T2[i][j][1]])
                        del T2[i][j]
                else:
                    j = j+1
        return m1, m2
    return 0, 0


for i in Emp:
    print(i, Emp[i])

print()
dec = input("Do you wanna Schedule a meeting?(y/n): ")
f = open('Meet.csv', 'w')
writer = csv.writer(f)
header = ["Employee Ids", "Meeting From", "Meeting To"]
writer.writerow(header)
Frm = ""
To = ""
while(dec == "y"):
    pos = schdMeet()
    if pos == (0, 0):
        print("Scheduling your Meeting is not possible")
    else:
        Frm, To = min_time(pos[0], pos[1])
    print()
    lid = lid.replace(" ", ",")
    writer.writerow([lid, Frm, To])
    dec = input("Do you wanna Schedule a meeting?(y/n): ")
f.close
