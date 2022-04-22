from datetime import datetime

def free_time(x,bounds,time):
        new=[]
        b_start=datetime.strptime(bounds[0],"%H:%M")
        b_end=datetime.strptime(bounds[1],"%H:%M")
        start=datetime.strptime(x[0][0],"%H:%M")
        end=datetime.strptime(x[len(x)-1][1],"%H:%M")
        min_start=(b_start-start).seconds/60
        #print(min_start)
        min_end=(b_end-end).seconds/60
        #print(min_end)
        if min_start >= float(time):
            new.append([bounds[0],x[0][0]])
        for i in range(len(x)-1):
            if ((datetime.strptime(x[i+1][0],"%H:%M")-datetime.strptime(x[i][1],"%H:%M")).seconds/60) >=float(time):
                new.append([x[i][1],x[i+1][0]])
        if min_end >= float(time):
            new.append([x[len(x)-1][1],bounds[1]])
        
        print(new)
        return new
        



def meeting_time(calendar1,calendar2,time):
        pres=[]
        final=[]
        #print(calendar1)
        #print(calendar2)
        for i in range(len(calendar1)):            
            for j in range(len(calendar2)):                
                if datetime.strptime(calendar1[i][1],"%H:%M")<=datetime.strptime(calendar2[j][1],"%H:%M"):
                    if datetime.strptime(calendar1[i][0],"%H:%M")>=datetime.strptime(calendar2[j][0],"%H:%M"):
                        if ((datetime.strptime(calendar1[i][1],"%H:%M")-datetime.strptime(calendar1[i][0],"%H:%M")).seconds/60) >= float(time) :
                            pres.append([calendar1[i][0],calendar1[i][1]])
                    else:
                        if ((datetime.strptime(calendar1[i][1],"%H:%M")-datetime.strptime(calendar2[j][0],"%H:%M")).seconds/60) >= float(time) :
                            pres.append([calendar2[j][0],calendar1[i][1]])
                else:
                    if datetime.strptime(calendar1[i][0],"%H:%M")>=datetime.strptime(calendar2[j][0],"%H:%M"):
                        if ((datetime.strptime(calendar2[j][1],"%H:%M")-datetime.strptime(calendar1[i][0],"%H:%M")).seconds/60) >= float(time) :
                            pres.append([calendar1[i][0],calendar2[j][1]])
        for i in range(len(pres)):
            if datetime.strptime(pres[i][0],"%H:%M")<datetime.strptime(pres[i][1],"%H:%M"):
                final.append([pres[i][0],pres[i][1]])
                        
        return final

    
person1=[['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
person2=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','16:30'],['17:30','18:00']]
working_hours_p1=['9:00','20:00']
working_hours_p2=['10:00','20:00']
time_def=30    


calendar1=free_time(person1,working_hours_p1,time_def)
calendar2=free_time(person2,working_hours_p2,time_def)
meetings=meeting_time(calendar1,calendar2, time_def)

for i in range(len(meetings)):
    print(i+1,'. possible time for the meeting is : ', meetings[i]);


# TODO: Updation, CSV Adding & Writing
# Durationr requires 4 hours