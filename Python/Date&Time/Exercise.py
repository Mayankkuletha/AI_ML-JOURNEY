#Checking we have surpassed an important date or not
import datetime

target_datetime= datetime.datetime(2020 , 1 , 2 , 12 ,30 , 1)
current_dateTime = datetime.datetime.now()

if target_datetime < current_dateTime :
    print("That essential and important time had already passed")
else :
    print("The time is not passed yet")