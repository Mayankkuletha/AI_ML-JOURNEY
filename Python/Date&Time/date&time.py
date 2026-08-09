# Date and Time using In python

import datetime

date = datetime.date(2026,5,31)
print(date) #will print date

time = datetime.time(12,30,6)
print(time) #will print above given time\

now = datetime.datetime.now() #We are acessing datetime module then datetime class it will give the current date and time in this format 2026-08-09 23:42:22.908021
print(now)

# to make in in certain format
now =  now.strftime("%H:%M:%S %m-%d-%Y") #23:46:28 08-09-2026
print(now)

target_datetime= datetime.datetime(2020 , 1 , 2 , 12 ,30 , 1)
# If we want to set both date and time
