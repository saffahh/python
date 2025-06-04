print("---BANK MANAGEMENT SYSTEM MENU---")
print("1.Create new account")
print("2.Deposit money")
print("3.withdraw money")
print("4.Display account details")
print("5.Exit")


accounts=[]
new_ac_no=1000
initial_bal=0
total_balance=0

choice=int(input("enter your choice:"))
while choice<=5:
    if choice=='1':
        name=input("enter your name: ")
        initial_balance=int(input("enter intial balance: "))
        initial_bal+=initial_balance                                                    #    *****************************correct if needed
        ac_no=new_ac_no
        new_ac_no+=1                               
        new_ac={"name":name,"ac_no":ac_no,"balance":initial_bal}
        accounts.append(new_ac)
        print(f"Account created successfully! Account Number: {ac_no} and initial balance: {initial_bal}")

    elif choice=='2':
        ac_no=int(input("enter your account number: "))

        for ac in accounts:
            if ac['ac_no']==ac_no:
                deposit_amnt=int(input("enter the amount to deposit"))
                if deposit_amnt>0:
                    total_balance=initial_bal+deposit_amnt
                    print("Deposit Successful ! New Balance:" ,total_balance)
                else:
                    print("enter a valid number")
            else:
                print("account not found")     

    elif choice =='3':
        ac_no=int(input("enter the account number: "))
        for ac in accounts:
            if ac==ac_no:
                withdraw_amount=int(input("enter the amount:"))
                if total_balance>withdraw_amount>0:
                    total_balance=total_balance-withdraw_amount
                    print("Withdrawal successful! New balance:",total_balance)
                else:
                    print("Insufficient balance.")    
            else:
                print("Account not found.")
    elif choice == '4':
        ac_no = input("Enter account number: ")
        for acc in accounts:
                if acc == ac_no:
                    print("--- Account Details ---")
                    print("name")
                    print("ac_no")
                    print("total_balance")
                else:
                    print("Account not found.")
                            
    elif choice == '5':
            print("exit")
else:
        print("invalid input")