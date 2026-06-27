#guess=input("enter")
#a=int(guess)
#print(type(a))

'''a = int("hello")

print(a)

print(type(a))'''

'''print(1 == False)'''

'''
guess = "45"

print(guess < 67)'''

'''
dice=input("enter: ")

while not dice.isdigit():
    dice=input("enter: ")
'''
'''dice=input("enter: ")
print(dice.isdigit())'''
import random
to_show=[]
list_options=["1","2","3","4","5"]
for i in range (0,3):
    unit=random.choice(list_options)
    to_show.append(unit)
print(to_show)