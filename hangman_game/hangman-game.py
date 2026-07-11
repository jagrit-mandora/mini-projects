import random

def initial_word():
    with open("hangman_words.txt","r") as file:
        words=file.read().splitlines()

    hangman_word=random.choice(words).lower()

    hangman_word=list(hangman_word)

    return hangman_word

def display_underscore(hangman_word):
    display=[]
    for i in range (0,len(hangman_word)):
        display.append("_")
    for i in display:
        print(i,end="")

    print()

    return display

def print_display(display):
    for i in display:
        print(i,end="")
    print()

def game_working(running,hangman_word,display,lives,guess_prev):
    hangman_photo= ["""
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                /|   |
                    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                /|\\  |
                    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                /|\\  |
                /    |
                    |
                =========
                """,
                """
                +---+
                |   |
                O   |
                /|\\  |
                / \\  |
                    |
                =========
                """
                ]
        
    while running:

        print(f"lives remaining: {lives}")

        print(hangman_photo[6-lives])
            
        print(f"PREVIOUS GUESSES ARE:")
        for i in guess_prev:
            print(i,end=" ")

        print()

        guess=input("Enter the guess: ").lower()
        while not guess.isalpha() or  not len(guess)==1:
            guess=input("Enter the guess: ").lower()

        if guess in hangman_word:
            for i in range (0,len(hangman_word)):
                if hangman_word[i]==guess:
                    display[i]=guess
            guess_prev.append(guess)
            print_display(display)
        elif guess in guess_prev:
            print(F"ALREADY GUESSES: {guess}")
            print_display(display)
        elif guess not in guess_prev:
            guess_prev.append(guess)
            print_display(display)
            lives-=1
            if lives==0:
                print(f"GAME OVER. NO LIVES LEFT")
                running=False
                break


        if "_" not in display:
            print("YOU WIN")
            lives1=6-lives
            print(f"NO OF LIVES USED: {lives1}")
            running=False




def main():
    want_to_play=True

    while want_to_play:
        want_play=input("ENTER Y TO CONTINUE AND N TO EXIT: ").lower()
        while want_play not in ["y","n"]:
            want_play=input("ENTER Y TO CONTINUE AND N TO EXIT: ").lower()

        if want_play=="n":
            want_to_play=False
            break

        running=True
        hangman_word=initial_word()
        display=display_underscore(hangman_word)
        lives=6
        guess_prev=[]

        game_working(running,hangman_word,display,lives,guess_prev)    
        


if __name__=="__main__":
    main()