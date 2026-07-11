# print("Times Up")

#countdown days:hour:minute:seconds
import time

print("time_to_calculate")

days=int(input("enter the days: "))
hour=int(input("enter the hour: "))
minutes=int(input("enter the minutes: "))
seconds=int(input("enter the seconds: "))

d=days*24*60*60
h=hour*60*60
m=minutes*60
s=seconds

countdown=d+h+m+s

for i in range(countdown,0,-1):
    seconds= i % 60
    minutes= (int(i/60)) % 60
    #hour= (int((int(i/60)) / 60))
    hour=int(i/3600)
    days=int(i/86400)
    # % 24 is excluded from hours as we dont have days and having % 24 makes it so that 86405
    # starts from 00:00:05.
    print(f"{days:02}:{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("Times Up")