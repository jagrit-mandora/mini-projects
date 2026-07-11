import random

rolling=True

rolled_dice_number=[]
rolled_dice_number_2=[]
sum_roll_history=[]

totalrolls=0


while rolling:

    dice_numbers=random.randint(1,6)
    dice_numbers2=random.randint(1,6)
    sum_roll=dice_numbers + dice_numbers2
    print(f"the number on dice is : {sum_roll}")

    rolled_dice_number.append(dice_numbers)
    rolled_dice_number_2.append(dice_numbers2)
    sum_roll_history.append(sum_roll)

    totalrolls+=1

    roll_again=input("enter y to continue and n to exit: ")
    while roll_again not in ("y","n"):
        roll_again=input("enter y to continue and n to exit: ")
    
    if roll_again=="n":
        rolling=False
    
print(f"Total numbers of roll: {totalrolls}")
print(f"The rolled results are : dice 1: {rolled_dice_number} and dice 2: {rolled_dice_number_2}")
print(f"Sum of 2 dice at each stage: {sum_roll_history}")

totalsum=0

for i in sum_roll_history:
    totalsum+=i

avgdice=totalsum/totalrolls

print(f"average of dice rolls is : {avgdice}")