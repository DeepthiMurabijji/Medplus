
# Step 1:

employeeData = [

    ["10:00", "18:00", "13:00", "14:00"],
    []

]

employeeDataMinutes = []

for x in employeeData:

    tempArr = [] 
    for y in x:

        temp = y.split(":")
        tempHours = int(temp[0]) * 60
        tempMinutes = int(temp[1])
        tempTotalTime = tempHours + tempMinutes

        employeeDataMinutes