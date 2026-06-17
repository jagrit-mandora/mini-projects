# in this we will try to find out the hypotenuse of the right angled triangle
# to find it we will use the formula : h=sqrt(a^2+b^2)

import math

a=int(input("enter side a : "))

b=int(input("enter side b : "))

h=math.sqrt(pow(a,2)+pow(b,2))

print(h)