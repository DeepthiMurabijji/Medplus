# The world is going to be attacked by the aliens. The space intelligence department has raised an alarm and the world armies are coming together to fight them. The planning and strategizing is being done to make the maximum impact on the alien ships. The deadly missiles are to be put into action. The missiles are targeted to destroy the alien ships in space and disable them to land on the Earth.


# The army is planning to launch the attack at A time (hh mm) to get an advantage. For each attack, they know the time the missile will require to hit the coming alien ship. They all are busy in preparation and want to know the time at which the blast will occur and the alien ship will be destroyed in pieces. Can you find the time of the blast ?


# Note: The World Army follows a 24-hour time format and you need to find the time of blast accordingly. The time will be in the hh mm format.




# Input Format
# The first line of input consists of the launch time in hh mm format separated by space.

# The second line of input consists of the travel time for the missile in hh mm format separated by space.



# Constraints
# 00<= hh <=23

# 00<= mm <=59



# Output Format
# Print the time at which the blast will occur and the spaceship will be destroyed.


lt = input()
tt = input()
lt = list(lt.split(' '))
tt = list(tt.split(' '))
DTH = int(lt[0])+int(tt[0])
DTM = int(lt[1])+int(tt[1])
DTH += DTM//60
print("dth: ",DTH)
DTM = DTM%60
print("dtm: ",DTM)
DTH = DTH%24
print("dthh:",DTH)
DTM = str(DTM)
DTH = str(DTH)
if len(DTM)==1:
    DTM = '0'+DTM
if len(DTH)==1:
    DTH = '0'+DTH
DT = DTH+' '+DTM
print(DT)