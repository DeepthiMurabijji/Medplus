
empList = [0, 1]

list2D = [

    [[540], [780, 840], [1080]],
    [[600], [780, 840], [1140]]

]

duration = 60

# Finding Maximum among the mployees 
'''
maximum = 0

for x in empList:
    for y in range(len(list2D[0]) - 1 ):
        if y == 0:
            diff = abs(list2D[x][y][0] - list2D[x][y+1][0])
            if diff > duration:
                if list2D[x][y][0] >= maximum:
                    maximum = list2D[x][y][0]
                    break
                
        else:
            diff = abs(list2D[x][y][1] - list2D[x][y+1][0])
            if diff > duration:
                if list2D[x][y][1] >= maximum:
                    maximum = list2D[x][y][1]
                    break

        y += 1

temp = []


for i in empList:

    temp.append(maximum)
    temp.append(int(maximum) + int(duration))
    list2D[i].append(temp)
    list2D[i].sort()
    print()

print(list2D)


print(maximum)
'''
def hrToMinString(str):

    strSplit = str.split(":")
    hours = int(strSplit[0])
    minutes = int(strSplit[1])

    retMinutes = hours * 60 + minutes
    print (type(retMinutes))
    return int(retMinutes)

print(hrToMinString('9:45'))
def hrToMinInteger(inte):

    inteStr = inte.split(".")
    inteFirst = int(inteStr[0])
    inteSecond = int(inteStr[1])
    inteTotal = inteFirst * 60 + inteSecond/100 * 60

    print(inteTotal)
    return (inteTotal)

hrToMinInteger('1.5')

def minutesToHours(inte):
    varMin = (inte % 60)/60
    varHours = inte//60
    varTotal = varMin + varHours

    return varTotal
#print(minutesToHours(90))

# duration=input("Enter the duration of the meeting: ")
# duration = hrToMinString(duration)
# print(duration)