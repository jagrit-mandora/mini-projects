def show_balance(bank_balance):
    print(f"The amount of balance in account: {bank_balance}")
    

def deposit(bank_balance):
    todeposit=input("Enter the amount of money to Deposit: ")
    while not todeposit.isdigit():
        todeposit=input("Enter the amount of money to Deposit: ")

    # USE TRY AND EXEPT BLOCK IF YOU WANT FLOAT AND DECIMAL NUMBERS

    money_to_deposit=int(todeposit)

    bank_balance+=money_to_deposit

    print(f"Amount of money Deposited: {money_to_deposit}")
    show_balance(bank_balance)
    return bank_balance

def withdraw(bank_balance):
    towithdraw=input("Enter the amount of money to Withdraw: ")
    while not towithdraw.isdigit():
        towithdraw=input("Enter the amount of money to Withdraw: ")

    money_to_withdraw=int(towithdraw)

    if money_to_withdraw>bank_balance:
        print("INSUFFICIANT BALANCE TRY AGAIN")
        return bank_balance
    elif money_to_withdraw<0:
        print("PLEASE ENTER A POSITIVE AMOUNT")
        return bank_balance
    
    bank_balance-=money_to_withdraw

    print(f"Amount of money Withdraw: {money_to_withdraw}")
    show_balance(bank_balance)
    return bank_balance

def main():
    running=True
    bank_balance=0
    
    while running:


        print("BANKING PROGRAM")
        print("1. BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")

        choice_1=input("ENTER choice:1 , 2, 3 or 4: ")
        while choice_1 not in ["1","2","3","4"]:
            choice_1=input("ENTER choice:1 , 2, 3 or 4: ")
        choice=int(choice_1)

        if choice==1:
            show_balance(bank_balance)
        elif choice==2:
            bank_balance=deposit(bank_balance)
        elif choice==3:
            bank_balance=withdraw(bank_balance)
        elif choice==4:
            running=False

if __name__=="__main__":    
    main()

# this 
# if __name__=="__main__":    
#    main()
# makes it so that this program will only run here and not run 
# when it is imported for its functions later.


