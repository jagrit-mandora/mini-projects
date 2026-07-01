import string
import random

def take_input():
    string_1=input("Enter the string to Encrypt or Decrypt: ")

    return string_1

def initialize():
    chars= " " + string.punctuation + string.digits + string.ascii_letters

    chars=list(chars)

    key=chars.copy()

    random.shuffle(chars)

    print(key)
    print()
    print(chars)
    return key,chars

def encryption(key,chars,string1):
    encrypt_string=[]

    for i in range (0,len(string1)):
        for j in range (0,len(key)):
            if key[j]==string1[i]:
                encrypt_string.append(chars[j])

    return encrypt_string

def decryption(key,chars,string1):

    decrypt_string=[]
    for i in range (0,len(string1)):
        for j in range (0,len(chars)):
            if chars[j]==string1[i]:
                decrypt_string.append(key[j])

    return decrypt_string


def main():
    key,chars=initialize()
    running=True
    while running:

        print("ENCRYPTION AND DECRYPTION PROGRAM")
        print("1. ENCRYPT STRING")
        print("2. DECRYPT STRING")
        print("3. EXIT")
        
        choice_1=input("ENTER choice:1 , 2 or 3: ")
        while choice_1 not in ["1","2","3"]:
            choice_1=input("ENTER choice:1 , 2 or 3: ")
        choice=int(choice_1)

        if choice==1:
            string1=take_input()
            encrypt_string=encryption(key,chars,string1)
            for i in encrypt_string:
                print(i,end="")
            print()
        elif choice==2:
            string1=take_input()
            decrypt_string=decryption(key,chars,string1)
            for i in decrypt_string:
                print(i,end="")
            print()
        elif choice==3:
            running=False

if __name__=="__main__":
    main()
