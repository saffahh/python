# accounts=[]

# while True:
#     print("---BANK MANAGEMENT SYSTEM MENU---")
#     print("1.Create new account")
#     print("2.Deposit money")
#     print("3.withdraw money")
#     print("4.Display account details")
#     print("5.Exit")

#     choice=(input("Enter your choice:"))

#     if choice=='1':
#         name=(input("Enter your name:"))
#         balance=int(input("Enter your initial balance:"))
#         ac_no=int(input("Enter your account number:"))
#         accounts.append({'name':name,'account_number':ac_no,'balance':balance})
#         print(f"Account created successfully!account_number:{ac_no} and initial_balance:{balance}")

#     elif choice=='2':
#         ac_no_to_find=int(input("Enter your Account number:"))
#         for i in accounts:
#             if i['account_number']==ac_no_to_find:
#                 deposit_amount=int(input("Enter the amount deposit:"))
#                 if deposit_amount>0:
#                     i['balance'] += deposit_amount
#                     print("Amount Deposited successfully.current balance is",i['balance'])
#                 else:
#                     print("Enter a valid number!")
#             else:
#                 print("Account not found")

#     elif choice=='3':
#         ac_no_to_find=int(input("Enter your Account number:"))
#         for i in accounts:
#             if i['account_number']==ac_no_to_find:
#                 withdraw_amount=int(input("Enter the amount to withdraw:"))
#                 if withdraw_amount>0:
#                     if withdraw_amount<=i['balance']:
#                         i['balance']-=withdraw_amount
#                         print("amount withdrawn successfully.current balance is",i['balance'])
#                     else:
#                        print("insufficient balance")

#                 else:
#                     print("enter a valid amount") 

#             else:
#                 print("account not found")     

#     elif choice=='4':
#         ac_no_to_find=int(input("Enter your Account number:"))
#         for i in accounts:
#             if i['account_number']==ac_no_to_find:
#                 print("here is the required details:")
#                 print("name:",i['name'])
#                 print("account number:",i['account_number'])
#                 print("current balance:",i['balance'])
#             else:
#                  print("account not found")  

#     elif choice=='5':
#             print("EXIT")              

# else:
#     print("invalid choice.")

# -------------------------------------------------------------------------------------------------------------------
#                                 LIBRARY MANAGMENT SYSTE

# Books=[]
# users=[]

# while True:

#     print("----MAIN MENU----")
#     print("1.ADMIN")
#     print("2.USER")   
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         username=(input("Enter the username:"))
#         password=(input("Enter the password:"))
#         if username=="admin" and password=="adminhere":
#             print("Successfully logined as admin")
#         else:
#             print("Incorrect username or password")
#             break

#         while True:
#             print("---ADMIN MENU---") 
#             print("1.ADD BOOK") 
#             print("2.UPDATE BOOK") 
#             print("3.DELETE BOOK")       
#             print("4.DISPLAY BOOK")
#             print("5.EXIT")  

#             option=int(input("enter your choice:"))
#             if option==1:
#                 id=int(input("Enter the book_id:"))
#                 for i in Books:
#                     if i['book_id']==id:
#                         print("id already exists")
#                         break
#                 else:
#                     title=(input("Enter the title of the book: "))
#                     author=(input("enter the name of the author:"))
#                     quantity=int(input("Enter the quantity of book:"))
#                     if quantity<0:
#                         print("print enter a positive number")
#                     else:    
#                         new_book={'book_id':id,'book_title':title,'book_author':author,'quantity':quantity}
#                         Books.append(new_book)
#                         print("book created successfully.")

#             elif option==2:
#                 book_id_to_update=int(input("enter the book id to be updated:"))
#                 for i in Books:
#                     if i['book_id']==book_id_to_update:
#                         print(f"current details of the book id {book_id_to_update} is:")
#                         print(f"Title:{i['book_title']},Author:{i['book_author']},Quantity:{i['quantity']}")
#                         i['book_title']=(input("enter the new title:"))
#                         i['book_author']=(input("enter the new author:"))
#                         i['quantity']=(input("enter the new quantity:"))
#                         print("book updated successfully.")
#                         print(f"updated details of the book id {book_id_to_update} is:")
#                         print(f"Title:{i['book_title']},Author:{i['book_author']},Quantity:{i['quantity']}")
#                     else:
#                         ("book not found")    

#             elif option==3:
#                 book_id_to_delete=int(input("Enter the book id to be deleted:"))
#                 for i in Books:
#                     if i['book_id']==book_id_to_delete:
#                         books.remove(i)
#                         print("book deleted successfully")
#                     else:
#                         ("book not found.")  
            
#             elif option==4:
#                 book_to_display=int(input("enter the book id to display:"))  
#                 for i in Books:
#                     if i['book_id']==book_to_display:
#                         print("Here is the details of the book with id",i['book_id'])
#                         print("Title of the book:",i['book_title'])
#                         print("Author of the book:",i['book_author'])
#                         print("quantity of the book:",i['quantity'])
#                     else:
#                         print("book not found")    

#             elif option==5:
#                 print("EXIT")
#                 break

#             else:
#                 print("invalid choice")    

#     elif choice==2:
#         print("------USER MENU------")
#         print("1.REGISTRATION")
#         print("2.LOGIN")
#         select=int(input("select your choice:"))
#         if select==1:
#             name=input("enter your name:")
#             age=input("enter your age:")
#             address=input("enter your address:")
#             phone=input("enter your phone number:")
#             for user in users:
#                 if user['phone_number']==phone:
#                     print("phone number already registered")
#                     break
#             else: 
#                 username=input("enter the uesername:") 
#                 for user in users:
#                     if user['username_']==username:
#                         print(" ERROR!!!Username already exists")
#                         break
#                 else:    
#                     password=input("enter the password:")
#                     new_user=({'main_name':name,'age_':age,'address_':address,'phone_number':phone,'username_':username,'password_':password}) 
#                     users.append(new_user)
#                     print("registration compleated successfully.")       

#         elif select==2:
#             username=input("enter your username:")
#             password=input("enter your password:")

#             for user in users:
#                 if user['username_']==username and user['password_']==password:
#                     print("you have successfully logged in.")
#                 else:
#                     print("user doesn't exists")
#                 while True:
#                     print("1.Display all books.")
#                     print("2.Search book by name.")  
#                     print("3.Exit")
#                     choose=int(input("Enter a choice:")) 
#                     if choose==1:
#                         print(Books)
#                     elif choose==2:
#                         title_=input("enter the title of the book you want to search:")  
#                         for i in Books:
#                             if i['book_title']==title_:
#                                 print("your book",i['book_title'],"is now available") 
#                                 print(f"Title:{i['book_title']},Author:{i['book_author']},Quantity:{i['quantity']}") 
#                             else:
#                                 print("its not available")

#                     elif choose==3:
#                         print("EXIT")
#                         break   

#                     else:
#                         print("invalid choice")                    
        
#         else:
#             print("invalid choice")

#     else:
#         print("invalid choice.")  
# 
# --------------------------------------1
# string=input("enter the string:")
# count=0
# for i in string:
#     for j in string:
#         if i==j:
#             count+=1
#         else:
#             count=0
# print(count)              
# -------------------------------------------------------
# s=input("enter the string: ")
# char_count={}
# for char in s:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char]=1

# for char in s:
#     if char_count[char]==1:
#         print(s.index(char))
#         break
# ---------------------------------------------------------------
nums=[1,3,4,5]
s=set()
for num in nums:
    if num>0:
        s.add(num)

c=1
while True:
    if c not in s:
        print(c)
        break
        c+=1

      

