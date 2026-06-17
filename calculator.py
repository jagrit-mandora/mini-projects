# I am thinking about making a calculator progrmae that can handel multiple variables at once . it will input no of variables 
# from user then run a loop that many times to have the user enter the values . i then we can make them enter the operations 
# we will need a mested loop but i dont know how we will deel with last variable . also i dont know how we will arange the 
# precidence and will we need to need to shift all values from there space and how.

# this logic is flawed as if the user needs to enter value one by one what use is this calculator.
# I should make the user enter the whole calculation and make them in a list or array then handel them later. (cant think of 
# logic for now)

#lets see if we make this programe

#i am making this calculator as i hae learnt the basic use of operators and if conditions.
# I am thinking of updating this program whenever i learn something new and it can be applied here.

# I am thinking of making a question bank for all my questions for now i think a text file will be enough but
# later i should make it better.

a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
op=str(input("enter the operation you want to perform available operations inlude (+, -, *, \, **) : "))

if op=="+":
    r=a+b
    print(f"{a} + {b} = {round(r,3)}")

elif op=="-":
    r=a-b
    print(f"{a} - {b} = {r}")

elif op=="*":
    r=a*b
    print(f"{a} * {b} = {round(r, 2)}")

elif op=="/":
    r=a/b
    print(f"{a} / {b} = {r}")

elif op=="**":
    r=a**b
    print(f"{a} ** {b} = {r}")

else :
    print(f"enter a valid operator: {op} is not a valid operator")




