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

    step=input("enter the steps you want to shift the encryption: ")
    while not step.isdigit() or not int(step)<24:
        step=input("enter the steps(less than 24) you want to shift the encryption: ")

    return step,string_1

def Encryption(step,string_1):
    character=[]

    step1=int(step)

    for i in string_1:
        x=ord(i)
        if x==32:
            ch=90
            character.append(ch)
        elif x+step1>122:
            y=(x+step1)-122
            ch=y+96
            character.append(ch)
        else:
            ch=x+step1
            character.append(ch)

    for i in character:
        print(chr(i),end="")
    
    return character

def decryption(step,charactor):
        character1=[]

        step1=int(step)


        for i in range (0,len(charactor)):
            x=charactor[i]
            if x==90:
                ch=32
                character1.append(ch)
            elif x-step1<97:
                y=(x-step1)+26
                ch=y
                character1.append(ch)
            else:
                ch=x-step1
                character1.append(ch)

        for i in character1:
            print(chr(i),end="")



def main():
    step,string_1=take_input()
    charactor=Encryption(step,string_1)
    print()
    decryption(step,charactor)

if __name__=="__main__":
    main()
