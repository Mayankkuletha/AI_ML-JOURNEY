# A Python Banking Program

def showBalance(balance):
    print(f"Your balance is ${balance:2f}")

def Deposit():
    amount= float(input(("Enter the amount you want to deposit")))
    print("Thanku for depositing")
    return amount

def Withdraw():
    amount= float(input(("Enter the amount you want to withdraw")))
    print("Withdrawl Sucessfull")
    return amount
    
def main():
    balance = 0 
    isRunning = True
    while isRunning:

        print("--------************------------")

        print("Welcome to Mayank Banking System")
        print("what do you want to perform")
        print("Enter 1 for Show Balance")
        print("Enter 2 for Deposit")
        print("Enter 3 for Withdraw")
        print("Enter 4 for Exit.")

        print("--------************------------")

        choice = int(input("Enter the value from 1-4 to perform the specific Functions"))

        if choice==1:
            showBalance()
        elif choice==2:
            balance+=Deposit()
        elif choice==3:
            balance-=Withdraw()
        elif choice == 4 :
            isRunning=False
        else :
            print("Please enter valid choice")

    print("Thanku for Using Banking")

if __name__=="__main__" :
    main()