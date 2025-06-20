# ---------------------------FUNCTION-----------------------------------------
# def square(num):
#     return num**2
# object=square(3)
# print("the square is:",object) 
# 
# ----------------------------------------------------------------------   
# def square(num):
#     return num**2
# number=int(input("enter the number:")) 
# b=square(number) 
# print("the square is:",b)  
# ---------------------------------------------------------------
# def count(string):
#     return len(string)
# print(count("functions"))
# print(count("safa"))    
# -------------------------------------------------------with argument with return type
# def square(num):
#     return num**2
# a=square(5)    
# print("answer is:",a)    

# --------------------------------------------------------with arg without return
# def greet(name):
#     print("hello",name)
# greet("anu")    
# --------------------------------------------------------without arg with return
# def get_message():
#     return "hi there"
# msg=get_message()
# print(msg)


# ------------------------------------------------------------without arg and without arg
# def print_num():
#     for i in range(1,10):
#         print(i)

# print_num()        
# ----------------------------------------------------------------------1
# def square(num):
#     return num**2
# number=int(input("enter the number:")) 
# b=square(number) 
# print("the square is:",b)
# -------------------------------------------------------------------------2
# def sum(num1,num2):
#     return num1+num2
# a=int(input("enter the num1:"))    
# b=int(input("enter the num2:"))    
# c=sum(a,b)
# print("the sum is:",c)
# ----------------------------------------------------------------------------3
# def uppercase(string):
#     return (string.upper())
# print(uppercase("happy birthday"))    
# -----------------------------------------------------------------------------4 arg without return
# def greet(name):
#     print("hello",name)
# greet("anu") 
# ----------------------------------------------------------------------------5
# def multiplication(num1,num2):
#     print(num1*num2)
# a=int(input("enter the number 1:"))
# b=int(input("enter the number 2:"))
# multiplication(a,b)
# -----------------------------------------------------------------------------6
# def prime(num):
#     if num%2==0:
#         print("it is prime")
#     else:
#         print("its odd")
# a=int(input("enter the number:"))
# prime(a)           
# 
# --------------------------------------------------------------------------------7 without arg with return
# def year():
#     return "2025"
# year_=year()
# print(year_)  
# -----------------------------------------------------------------------------------8
# def welcome():
#     return "welcome to visual code studio"
# msg=welcome()
# print(msg)     
# ---------------------------------------------------------------9
# def factorial():
#     fact=1
#     for value in range(1,a+1):
#         fact=fact*value
#         return(fact)
# a=int(input("enter your number: "))
# ans=factorial()
# print("factorial is:",ans)        


#----------------------------------------------------------------------------10 without arg without return
# a=input("enter your name:")
# def name():
#     name()
# print(a)    
# ---------------------------------------------------------------------11
# def print_num():
#     for i in range(0,11):
#         print(i)

# print_num()  
# -------------------------------------------------------------------------------
# def function(n1,n2=20):
#     print("num 1 is",n1)
#     print("num 2 is",n2)
# print("passing only 1 argument")
# function(30)    

#  --------------------------------------------keyword argumenr
# def function(n1,n2):
#     print("num 1 is",n1)
#     print("num 2 is",n2)
# print("without using keyword")
# function(n2=2,n1=2) 
# ------------------------------------------------- anonymous function
# add=lambda arg1,arg2:arg1+arg2
# print("value of the fnction is",add(20,10))
# -------------------------------------------------------function with another function
# def word():
#     string='python'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()   
# ---------------------------------------------reccursive function
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))

# num=3
# print("factorial of",num,"is",factorial(num))      
# ----------------------------------------------------------1
# def max():
#     list=[9,3,4,5,1] 
#     a=list[0]
#     for i in list:
#         if i>a:
#             a=i
#         return a 
# ans=max()        
# print("max num is",ans)           

# ------------------------------------------------------------2
# def reverse():
#     b=""
#     for i in a:
#         b=i+b
#     return b
# a=input("enter the string:") 
# c=reverse()
# print("rev is:",c)       
# ----------------------------------------------------------3
# def vowels():
#     a=["a","e","i","o","u"]
#     b=0
#     for i in string:
#         if i in a:
#             b+=1
#     return b
# string=input("enter the string:") 
# c=vowels()
# print("vowels in string are",c)   
# -----------------------------------------------------------4
# def palindrome():
#     b=a[::-1]  
#     if a==b:
#         print("its a palindrome")
#     else:
#         print("its not a palindrome")
#     return 
# a=input("enter the string:")    
# palindrome()   
# -----------------------------------------------------------------5
# def even():
#     b=[1,2,3,4,5]
#     a=[]
#     for i in b:
#         if i%2==0:
#             a.append(i)
#     return a  
# c=even()
# print("even numbers are",c)
# ------------------------------------------------------------------------6
# -------------------------------------------------------------------------7
# def add(a,b):
#     return a+b    

# def sub(a,b):
#     return a-b    

# def mul(a,b):
#     return a*b     

# def div(a,b):
#     if b==0:
#         return "division by 0 is not possible"
#     return a/b     

# print("CALCULATOR")
# print("1.ADD")
# print("2.SUBTRACTION")
# print("3.MULTIPLICATION")
# print("4.DIVISION")
# print("5.EXIT")

# choice=int(input("enter your choice:"))
# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))

# if choice==1:
#     print("answer is:",add(a,b))
# elif choice==2:
#     print("answer is:", sub(a,b))
# elif choice==3:
#     print("answer is:",mul(a,b))
# elif choice==4:
#     print("answer is:",div(a,b))

# elif choice==5:
#     print("EXIT") 
# else:
#     print("invalid input")               
# -------------------------------------------------------------------------------
#  add=lambda arg1,arg2:arg1+arg2
# print("value of the fnction is",add(20,10))
# --------------------------------------------------------------------------lambda 1
# square=lambda n1:n1*n1
# n1=int(input("enter the number:"))
# print("the square of",n1,"is:",square(n1))
# -------------------------------------------------------------------------2
# even=lambda a: "even" if a%2==0 else "odd"
# a=int(input("enter the number:"))
# print("the answer is",even(a))
# --------------------------------------------------------------------3
# greater=lambda a,b: "a is greatest" if a>b else "b is the greatest"
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print("the answer is",greater(a,b))
# ----------------------------------------------------------------------4
# string=lambda a: "yes" if a[0]=='a' else "no"
# a=input("enter the string:")
# print(string(a))
# # ---------------------------------------------------------------reccursive 1
# def nto1(n):
#     if n>0:
#         print(n)
#         nto1(n-1)
# nto1(10)        
# ---------------------------------------------------------------------2
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)  
# n=int(input("enter the number:"))
# print("answer is",sum(n))       
        
# -------------------------------------------------------------------3
# def sumdigit(n):
#     if n==0:
#         return n
#     else:
#         return (n%10)+sumdigit(n//10)
# n=int(input("enter the digit:",))
# print("sum of the digits is:",sumdigit(n))            

# -----------------------------------------------------------------------4
# def reverse(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[::-1] 
# s=input("enter the string:")
# print("the reverse is:",reverse(s))  
# -----------------------------------------------------------------------------type error
# x=5
# y="hello"                            ------------------------typeerror
# z=x+y
       
# x=5
# y="hello"
# try:
#     z=x+y

# except TypeError:
#     print("error:cannot add an int and a str")    
# --------------------------------------------------------------------------------- catching exceptions
# a=[1,2,3]
# try:
#     print("second elememt",a[1])
#     print("forth element",a[3])

# except:
#     print("an error occured")

# a=[1,2,3]
# try:
#     print("second elememt",a[1])                     
#     print("forth element",a[3])

# except Exception as e:                 ------------------------------Exception statement
#     print(e)

# ----------------------------------------------------else
# ----------------------------------------------------finally

# -----------------------------------------------------------------raising exception
# try:
#     raise NameError("hi there")

# except NameError:
#     print("an exception")
#     raise    

# --------------------------------------------------------------



