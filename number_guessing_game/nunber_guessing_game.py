import random

print("welcome to the number guessing game")
print("please enter your guess")

lowest_number=1
highest_number=100

answer=random.randint(lowest_number,highest_number)

guesses=0

is_running=True

while is_running and guesses<10:

    guess=input("Please enter the guessed number: ")
    
    if guess.isdigit():
        guess= int(guess)
        if guess < lowest_number:
            print(f"INPUT IS TOO LOW. IT SHOULD BE HIGHER THAN {lowest_number}")
        elif guess > highest_number:
            print(f"INPUT IS TOO HIGH. IT SHOULD BE LOWER THAN {highest_number}")
        elif guess == answer:
            print("CORRECT ANSWER")
            is_running=False
        elif guess < answer:
            print("CORRECT ANSWER IS HIGHER THAN GUESS")
        elif guess > answer:
            print("CORRECT ANSWER IS LOWER THAN GUESS")
        else:
            print("TRY AGAIN")
        guesses+=1
    else:
        print("Please enter a valid number")
    
print(f"No of guesses: {guesses}")

