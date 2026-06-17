import time

my_time=int(input("Enter the time in seconds: "))
end_time=3
for i in range (my_time,0,-1):
    print(i)
    time.sleep(my_time)

print("ok")