def take_input():
    while True:
        string_1=input("Enter the string to Encrypt: ").lower()

        valid=True

        for i in string_1:
            if not (i.isalpha()==True or i==" "):
                valid=False
                break

        if valid:
            break

        print("INVALID INPUT. TRY AGAIN")

    return string_1


def main():
    import string
    import random
    chars= " " + string.punctuation + string.digits + string.ascii_letters

    chars=list(chars)

    key=chars.copy()

    random.shuffle(chars)

    string1=take_input()

    

main()