#Working of an ATM machine using python
#Last updated: 27.01.2020

print("ATM MACHINE")
print("Welcome to National Bank of UAE")
print("Choose your Language")
print("1. ENGLISH")
print("2. ARABIC")
print("3. OTHER")

language=int(input("Please enter your preferred language"))

if language==(1,2,3):   #Only English Language works
    print("swipe your card here")
    
ATM_Pin=9999
#Here we are storing pin ATM_Pin

transaction=["balance enquiry", "Deposit", "Change my pin",
             "transfer money", "QUIT"]

#so here we are storing all transaction
Balance=10000
pin=int(input("Enter your Pin To PROCEED:"))
if pin==9999:
    print("Choose your transaction:")
    print("1. Balance Enquiry")
    print("2. Withdraw Money")
    print("3. Deposit")
    print("4. Change my pin")
    print("5. Transfer money")
    print("6. QUIT")
    trans=int(input(" "))
    if trans==1:
        print("Your Balance is:",Balance)
    elif trans==2:
        amount=int(input("Enter your amount to proceed"))
        if amount > 0:
                  print("Collect your cash, Thanks for using National Bank of UAE")
                  Balance=Balance-amount
                  print("Your Balance is:",Balance)
        else:
                  print("Enter valid amount to proceed")
    elif trans==3:
        deposit=int(input("Enter your amount to deposit:"))
        if deposit>0:
            print("AMOUNT HAS BEEN SUCCESFULLY DEPOSITED, THANKS FOR USING National Bank of UAE")
            Balance=Balance+deposit
            print("Your Balance is:",Balance)
        else:
            print("Enter valid amount to proceed")

    elif trans==4:
        change_pin=int(input("ENTER YOUR NEW PIN"))
        if change_pin>=0:
            print("Your PIN has been succesfully changed! Thanks for using National Bank of UAE.")
        else:
            print("Enter valid PIN to proceed.")
    elif trans==5:
        transfer=int(input("Enter your amount to transfer"))
        if transfer>0:
            print("Your money has been transfered! Thanks for using National Bank of UAE")
            Balance=Balance-transfer
            print("Your Balance is:",Balance)
        else:
            print("Enter valid amount to proceed")
    elif trans==6:
        exit()
else:
    print("Wrong Password..........!")
