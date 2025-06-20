# import module
# result=module.square(3)
# print(result)


# import math
# print(math.e)

# import math as mt
# print(mt.e)

# import time
# print(time.asctime(time.localtime(time.time())))

# import time

# for i in range(0,5):
#     print(i)
#     time.sleep(5)    

# import datetime
# print(datetime.datetime.now())

# import datetime
# print(datetime.datetime(2020,12,4))

# import calendar
# cal=calendar.month(2025,6)
# print(cal)

# import calendar
# cal=calendar.calendar(2025)
# print(cal)



# -------------------------------------------------------------------oops ----------self parameter

# class Employee:
#     id=10
#     name="john"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()        


# --------------------------------------------------------------------------------
# class Employee:
#     id=10
#     name="john"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display() 
# del emp.id
# del emp.name
# emp.display()


# ------------------------------------------------------------------parametriced
# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=car("toyota",2016)
# c1.display()            

# ---------------------------------------------------------------------non- parametriced
# class Student:
#     def __init__(self):
#         print("non para metriced constuctor")
#     def show(self,name):
#         print("hello",name)
# student=Student()
# student.show("john")            

# -----------------------------------------------------------------default constructor
# class Student:
#     roll_no=101
#     name="joseph"
#     def display(self):
#         print(self.roll_no,self.name)
# st=Student()
# st.display()  
# ------------------------------------------------------------   
# class Student:  
#     def __init__(self,name,id,age):
#         self.name=name
#         self.age=age
#         self.id=id

# s=Student("safa",21,1)

# print(getattr(s,"name"))
# setattr(s,"age",23)
# delattr(s,"age")
# print(s.age)
# print(getattr(s,"age"))
# print(hasattr(s,'id'))

# ---------------------------------------------------------------1
# class Student:
#     roll_no=101
#     name="joseph"
#     mark=90
#     def display(self):
#         print(self.roll_no,self.name,self.mark)
# st=Student()
# st.display()

# ---------------------------------------------------------------------2
# class Rectangle:
#     length=10
#     breadth=2
#     def display(self):
#         print(self.breadth*self.length)
# area=Rectangle()
# area.display()       
# 
# ----------------------------------------------------------------------3
# class Car:
#     brand="bmw"
#     model=2021
#     year=2024
#     def display(self):
#         print(self.brand,self.model,self.year)
# car=Car()
# car.display()        
# ----------------------------------------------------------------------4
# class Person:
#     name="safa"
#     age=21
#     def display(self):
#         if(self.age)>=18:
#             print("you are eligible to vote")
#         else:
#             print("you are not eligible to vote")
# person=Person()
# person.display()      
# 
# ---------------------------------------------------------------------------5


# class BankAccount:
   
#     def __init__(self,account_holder,initial_balance):

#         self.account_holder=account_holder
#         if initial_balance>=0:
#             self.balance=initial_balance
#         else:
#             print("initial balance cannot be 0") 

#     def display(self):
#         print(self.account_holder,self.balance)


#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print("amount deposited,new balance:",self.balance)

#         else:
#             print("enter a positive number.")    

#     def withdraw(self,amount):
#         if amount<0:
#             print("enter a positive number.")
#         elif amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             print("amount withdrawn successfully.current balance is:",self.balance)


#     def check_balance(self):
#         print("current balance of",self.account_holder,"is:",self.balance)



# john_account=BankAccount('john',500) 
# john_account.display()
# john_account.check_balance()
# john_account.deposit(100)
# john_account.withdraw(100)
# jane_account=BankAccount('jane',1000)
# jane_account.display()
# jane_account.deposit(100)


# --------------------------------------------------------------------------------single inheritence
# class Animal:
#     def speak(self):
#         print("animal speaking")              ------------------------base class

# class Dog(Animal):
#     def bark(self):                            ---------------------derived class
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()                

# --------------------------------------------------------------------------------multi level inheritence
# class Animal:
#     def speak(self):
#         print("animal speaking")              

# class Dog(Animal):
#     def bark(self):                            
#         print("dog barking")


# class DogChild(Dog):
#     def eat(self):
#         print("eating bread")

# d=DogChild()
# d.bark()
# d.speak()  
# d.eat() 
# -----------------------------------------------------------------------------multiple inheritence

# class Calculation1:
#     def sum(self,a,b):
#         return a+b
# class Calculation2:
#     def product(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def div(self,a,b):
#         return a/b 

# d=Derived()
# print(d.sum(1,2))
# print(d.product(2,3))
# print(d.div(4,2))

# ------------------------------------------------------------------------hierarchichal inheritence
# class Parent:
#     def fun1(self):
#         print("this function is in parent class")

# class child1(Parent):
#     def fun2(self):
#         print("this function is in child1")

# class child2(Parent):
#     def fun3(self):
#         print("this function is in child2")   

# a=child1()
# a.fun1()
# a.fun2()

# b=child2()
# b.fun1()
# b.fun3()
# -------------------------------------------------------hybrid

# class Parent:
#     def fun1(self):
#         print("this function is in parent class")

# class child1(Parent):
#     def fun2(self):
#         print("this function is in child1")

# class child2(Parent):
#     def fun3(self):
#         print("this function is in child2") 

# class derived(Parent,child1):
#     def fun4(self):
#         print("this is multiple inheritence") 


# a=derived()
# a.fun1()

# -------------------------------------------------------POLYMORPHISM
# class Birds:
#     def speak(self):
#         print("koooo")

# class Dog(Birds):
#     def speak(self):
#         print("bowww")
# d=Dog()
# d.speak()      
# 
# -------------------------------------------------------------------eg 2
# class Bank:
#     def get(self):
#         return 10

# class SBI(Bank):
#     def get(self):
#         return 2

# class ICICI(Bank):
#     def get(self):
#         return 2

# b1=Bank()
# b2=SBI()
# b3=ICICI()

# print("bank:",b1.get())
# print("bank:",b2.get())
# print("bank:",b3.get())

# --------------------------------------------------------
class Bird:
    def intro(self):
        print("birds")

    def flight(self):
        print("bird can fly")
class Sparrow(Bird):
    def flight(self):
        print("sparrow")

class Ostrich(Bird):
    def flight(self):
        print("ostrich")


a=Bird()
b=Sparrow()
c=Ostrich()

a.intro()
a.flight()
b.flight()
c.flight()
c.intro()


    

               



