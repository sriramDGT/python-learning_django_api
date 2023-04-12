print("Welcome to SBI Bank \n \nInsert Your Card")

password=1234
choice = 0
balance=10000
pin=int(input("\nEnter Your four Digit Pin :"))

if pin==password:

    while choice !=4:
        print("\n")
        print("--Menu--")
        print("1.Balance")
        print("2.Deposit")
        print("3.WithDraw")
        print("4.Cancel")

        choice=int(input("\nEnter You option:\n"))

        if choice==1:
            print("\nBalance = Rs:",balance)

        elif choice==2:
            dep=int(input("\nEnter Your deposit :Rs: "))
            balance +=dep
            print("\nDeposited amount :R",dep)
            print("\nBalanace = R",balance)

        elif choice==3:
            wit=int(input("Enter the amount of withdraw :Rs:"))
            balance -=wit
            print("\WithDraw amount:Rs:",wit)
            print("Balance =R",balance)

        elif choice ==4:
            print("\nSession Ended... Good Bye...! :)")

        else:
            print("\nInvaild Input")
else:
    print("\nPin Incorrect ! Try Again")