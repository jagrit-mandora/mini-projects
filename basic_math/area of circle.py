#now we will calculate the area of a circle 
#the formula fo this is area = pi* r^2


import math

radius=float(input("enter the radius of the circle you want the area calculated in units : "))

area=math.pi* pow(radius,2)

print(f"the area of the circle of radius {radius} units is {round(area,4)} units^2")
