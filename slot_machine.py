import random

def show_balance(balance):
    print(f"Balance : {balance}")

def spin():
    pass

def main():
    balance=100

    list_options=["1","2","3","4","5"]

    running=True

    while running:
        to_show=[]

        show_balance(balance)

        start=True
        while start:
            start_program=input("Enter y to continue and n to exit: ").lower()
            
            if start_program=="y":
                start=False
                continue
            elif start_program=="n":
                start=False
                running=False
            else:
                print("ENTER Y OR N")

        if running==False:
            print("THANKS FOR PLAYING THE GAME")
            break


        bet_run=True

        while bet_run:
            bet_go=input("input the bet: ")
            try:
                bet=float(bet_go)
            except ValueError:
                continue
            
            if bet<0:
                print("PLEASE ENTER A POSITIVE NUMBER")
                continue
            elif bet>(balance/2):
                print("PLEASE INPUT VALID NUMBER: ")
                continue
            else:
                bet_run=False


        for i in range (0,3):
            unit=random.choice(list_options)
            to_show.append(unit)

        print(to_show)

        if to_show[0]==to_show[1] and to_show[1]==to_show[2]:
            if to_show[0]=="1":
                balance+=(bet*0)
            elif to_show[0]=="2":
                balance+=(bet*1)
            elif to_show[0]=="3":
                balance+=(bet*2)
            elif to_show[0]=="4":
                balance+=(bet*5)
            elif to_show[0]=="5":
                balance+=(bet*10)
        else:
            balance-=(bet*2)

        if balance==0:
            print("BALANCE IS ZERO : GAME OVER")
            running=False

main()
