#To make this said calculator we need it so that when a amount say 100 is put
# and the interest  is 1 % per day then every day 1% of the amount that day is 
#calculated and added. The amount changes everyday.

import math

while True:
    try:
        Amount_of_principle=float(input("Enter the amount of money "))
        compound_intrest=float(input("Enter the interest rate"))
        Time=float(input("Enter the time in years"))
        if Amount_of_principle<=0:
            print("please enter a valid principle")
        elif compound_intrest<=0:
            print("please enter a valid interest rate")
        elif Time<=0:
            print("enter valid time")
        else:
            amount_to_pay=Amount_of_principle*((1+(compound_intrest/100)**Time))
            print(f"{amount_to_pay}")
            break
    except:
        print("Please enter the correct values")
