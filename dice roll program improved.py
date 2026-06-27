import random

dice_rolls_number=input("Enter the number of dice to roll at once: ")
while not dice_rolls_number.isdigit():
    dice_rolls_number=input("Enter the number of dice to roll at once: ")

number_of_times_to_roll=0

how_many_to_roll=input("Enter the number of times to roll the dice: ")
while not how_many_to_roll.isdigit():
    how_many_to_roll=input("Enter the number of times to roll the dice: ")

rolling=True

list_of_all_dice=[]

while rolling and number_of_times_to_roll<int(how_many_to_roll):

    number_of_times_to_roll+=1


    list_of_dice=[]

    for i in range (0,int(dice_rolls_number)):
        dice_numbers=random.randint(1,6)
        list_of_dice.append(dice_numbers)

    list_of_all_dice.append(list_of_dice)

print(f"dice rolled till now: {list_of_all_dice}")

'''    roll_again=input("enter y to continue and n to exit: ")
    while roll_again not in ("y","n"):
        roll_again=input("enter y to continue and n to exit: ")

    if roll_again=="n":
        rolling=False
        break
'''
#print(f"dice rolled till now: {list_of_all_dice}")