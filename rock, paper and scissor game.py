import random
options=["rock","paper", "scissor"]

Wins=0
losses=0
ties=0

running=True
while running:
    
    player=input("Enter the choice from (rock, paper and scissor): ").lower()
    while player not in options:
        player=input("Enter the choice from (rock, paper and scissor): ").lower()
    computer=random.choice(options)

    print(f"players choice: {player}")
    print(f"computers choice: {computer}")

    if player==computer:
        print("ITS A TIE")
        ties+=1
    elif player=="rock" and computer=="scissor":
        print("YOU WIN")
        Wins+=1
    elif player=="scissor" and computer=="paper":
        print("YOU WIN")
        Wins+=1
    elif player=="paper" and computer=="rock":
        print("YOU WIN")
        Wins+=1
    else:
        print("YOU LOST")
        losses+=1

    play_again=input("please enter y to continue and n to exit: ").lower()
    while play_again not in ("y", "n"):
        play_again=input("please enter y to continue and n to exit: ").lower()
    if play_again=="n":
        running=False

print(f"The Wins are : {Wins}")
print(f"The Losses are : {losses}")
print(f"The Ties are : {ties}")