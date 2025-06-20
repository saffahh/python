# fruits="watermelon"
#print(len(fruits))
# print(fruits[0])
# print(fruits[-1])
# print(fruits[0:5])
# print(fruits[0:5:2])
# print(fruits[::])

# fname="safa"
# lname="latheef"
# print(fname+' '+lname)

# print(fname*4)

# text="hello guyss,goodmorning...!"
# print(text.upper())

# text="HELLOOO..!EVERYONE.."
# print(text.lower())

# text="hello guyss,goodmorning...!"
# print(text.replace("he","me"))

# text="hello guyss,goodmorning...!"
# print(text.count("l"))

# text="hello guyss,goodmorning...!"
# print(text.find("guyss"))

#-----------------------------------------------------------------------list

# vowels=['a','e','i','o','u']

# vowels[2]='b'
# consanants=['b','c']
# vowels.append('o')
# vowels.insert(3,'o')
# vowels.extend(consanants)
#vowels.pop(1)
# del vowels[0:3]
# vowels.remove('a')
# vowels.reverse()

# print(vowels)


# list1=[1,2,3,4,5,6,7]
# list2=[5,6,7,8,9,10,11,12]
# # l=list1*2
# l=list1+list2

# print(l)
# a=len(list1)
# for i in list1:
#     print(i)
# print(5 in list1)
# print(max(list1))
# print(min(list1))
# l=set(list1).intersection(list2)
# l=set(list1) & set(list2)
# print(l)
# -----------------------------------------------------------------------------------TUPLE
# letters=("a","b","c","d","e","f")
# print(letters[0])
# print(letters[-1])
# print(letters.count('b'))
# print(letters.index('a'))
# letters=letters*3
# print("new tuple is",letters)

# letters=("a","b","c","d","e","f")
# for letter in letters:
#     print(letter)

# letters=("a","b","c","d","e","f")
# print('a' in letters)
# print('g' in letters)

#letters=set(["a","b","c","d","e","f"])
# print(letters)
# print(type(letters))
# for i in letters:
#     print (i)
# letters.add("z")
# print(letters)

# letters.update(["z","y","x"])
# print(letters)
# letters.discard("b")
# letters.discard("z")


#letters.remove("b")
# letters.remove("z")
# print(letters)

# num1={"1","2","3"}
# num2={"3","4","5"}
# # print(num1|num2)
# print(num1&num2)

#------------------------------------------------------------------------DICTIONARY
# stdnt_id={1:"safa",2:"shahaba",3:"farsana"}
#print(stdnt_id)
# stdnt_id[2]="shabana"
# print(stdnt_id)
#print(stdnt_id[1])
# del stdnt_id[2]
# print(stdnt_id)
# stdnt_id={1:"safa",2:"shahaba",3:"farsana"}
#stdnt_id[4]="shabana"
#print(stdnt_id)
# for i in stdnt_id:
#     print(stdnt_id[i])

# for i in stdnt_id:
#      print([i])


# ---------------------------------------------------------------------------------input value

# a=int(input("enter the first number : "))
# b=int(input("enter the second number : "))

# # print("{} & {}".format(a,b))

# print(f"{a} & {b}")

#-----------------------------------CONDITIONAL STATEMENT--------------------------------------------------------

# i=10
# if(i>15):
#     print("10 is greater than 15")
# print("10 is less than 15")    
# --------------------------------------IF ELSE---------------------------------------------------------------
# i=10
# if(i>15):
#      print("10 is greater than 15")

# else:
#        print("10 is less than 15") 
#        print("i am lesserrr")   
  
# print("i am not in the if-else block")
# ------------------------------------------NESTED IF--------------------------------------------------
# i=10
# if(i==10):
#     if(i<15):
#         print("i is lesser than 15")

#     if(i<12):
#         print("i is smaller than 12 too")

#     else:
#         print("i is greater than 15")        

# ---------------------------------------------ELIF------------------------------------

# i=20
# if(i==10):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print("i is 20")
# else:
#     print("i is not present")            


# -------------------------------------------------even or odd---------------------------------------------


# a = int(input("enter the number : "))

# if(a%2==0):
#     print("the number is even")
# else:
#     print("the number is odd")    

# -------------------------positive or negetive----------------------------------------

# a=int(input("enter the number"))

# if(a>0):
#     print("the number is positive")

# elif(a<0):
#     print("the number is negetive")

# else:
#     print("the number is 0")        

# -----------------------------------------------------------VOWELL-----------------------------------


# a=(input("enter the letter:"))
# vowels=["a","e","i","o","u"]
# if(a in vowels):
#     print("the letter is a vowel")
# else:
#     print("the letter is a consanant")    

# -------------------------------------------grade test-------------------------

# a=int(input("enter the marks of the student:"))

# if(100>=a>=90):
#     print("the grade is A+")

# elif(90>a>=80):
#     print("the grade is B+ ")

# elif(80>a>=70):
#     print("the grade is C+")

# elif(70>a>=0):
#     print("the student is FAILEEDDDD") 

# else:
#     print("the mark entered is invalid") 


#--------------------------------------------------------------CALCULATOR-------------------

# print("CALCULATOR")
# print("OPERATIONS ARE:")
# print(" 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION")

# a=int(input("choose your operation : "))

# b=int(input("enter the first number :"))
# c=int(input("enter the second number : "))

# if(a==1):
#     print("the sum is:",b+c)
# elif(a==2):
#     print("the value is: ",b-c)
# elif(a==3):
#     print("the product is:",b*c)
# elif(a==4):
#     if(c==0):
#         print("division by 0 is not possible")
#     else:
#         print("the value is :",b/c)    
    
# else:
#     print("the value is invalid")               

#-----------------------------------greatest number in 3------------------------------------------------------------

# a=int(input("enter the first number : "))
# b=int(input("enter the second number : "))
# c=int(input("enter the third number : "))

# if(b<a>c):
#     print("a is the greatest")
# elif(a<b>c):
#     print("b is the greatest ")
# elif(a<c>b):
#     print("c is the greatest") 
# elif(a==b==c):
#     print("all are equal")
# else:
#     print("2 numbers are equal")           

# ---------------------------------------------------------leapyear----------------

# a=int(input("enter the year:"))
# if(a%4==0):
#     print("its a leap year")
# else:
#     print("its not a leap year")    


# -----------------------------even numbers of list-------------------------------------------

# num=[1,2,3,4,5,6,7,8,9,10]
# for n in num:
#     if(n%2==0):
#         print(n)

# ----------------------------------------loopp--------------------------------

# numbers=[1,2,3,4,5,6]
# square=0
# squares=[]

# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("the lis of squares is:",squares)

# ------------------------------------------loop

# string="python loop"
# for s in string:
#     if s=="o":
#         print("if block")
# else:
#     print(s)     
# -------------------------------------------
# print(range(15))   

# print(list(range(15)))
# print(list(range(4,15)))
# print(list(range(5,25,5)))
# -------------------------------------for loop range

# tuple=("safa","shaha","shaba","moh")
# for iterator in range(len(tuple)):
#     print(tuple[iterator].upper())

# ----------------------------------sum using for loop range----------------------------

# a=int(input("enter your range:"))
# num=0
# for value in range(a+1):
#     num=num+value

# print("the sum is:",num)

# -----------------------------------------------------------------mulptiplication

# a=int(input("multiplication table of: "))
# num=0
# for value in range(10+1):
#     num=value*a
#     print(value,"*",a ,"=",num)
# --------------------------------------------------factorial------------
# a=int(input("enter the number :"))
# num=1
# for value in range(1,a+1):
#     num=num*value
# print(num)    
# -------------------------------------------fibanocci
# a=int(input("fibanocci series..:"))
# b=0
# c=1
# d=0
# z=[]
# z.append(b)
# z.append(c)
# for i in range(1,a-1):
#     d=b+c
#     b=c
#     c=d
#     z.append(d)
# print(z)    
# -------------------------------------------------------sum of even nums upto n
# a=int(input("enter the limit: "))
# b=0
# for i in range(1,a):
#     if i%2==0:
#         b=b+i
# print(b)        
# -------------------------------------------------------------------------------vowels in a string
# a=(input("enter the string: "))
# v=('a','e','i','o','u')
# b=0
# for i in a:
#     if i in v:
#         b=b+1
# print(b)        

# -----------------------------------------------max no in list
# a=[1,2,3,4,5,6,7,60]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)    
# --------------------------------------------------product of all numbers
# a=[1,2,3,4,5]
# b=1
# for i in a:
#     b=b*i
# print(b)    
# ----------------------------------------------------reverse of a string
# a=(input("enter the string: "))
# b=""
# for i in a:
#     b=i+b
    
# print(b)    
# ------------------------------------------------charecters at even position
# a=input("enter the string: ")
# print("the charecters at even positions are:")
# for i in range(len(a)):
#     if i%2==0:
#         print(a[i]) 

 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>COMMON ELEMENTS INA LIST

# List1=[1,2,3,4,5]
# List2=[2,4,5,6,7]
# common_elmnts=[]
# for i in List1:
#     if i in List2:
#         common_elmnts.append(i) 
# print(common_elmnts)    

# -------------------------------------------WHILE LOOP--------------------------

# count=0
# while count<5:
#     count=count+1
#     print(count)
    
    
# else:
#     print("loop compleated")    



# -------------------------------------------10 TO 1-------------------------

# count=11
# while count>1:
#     count=count-1
#     print(count)
# else:
#     print("finished")    

# ----------------------------------------sum of  digits
# num=int(input("enter the number:"))
# sum=0
# while num>0:
#     d=num%10
#     sum+=d
#     num//=10
# print(sum)    

# -------------------------------------------palindrome
# a=(input("enter the word: "))
# b=a[::-1]
# while a==b:
#     print("its a palindrome")
#     break
# else:
#     print("its not palindrome")    
# ------------------------------------------------count nums of digits
# num=int(input("enter the number: "))
# count=0
# while num>0:
#     num//=10
#     count+=1
# print(count)    
# --------------------------------------QUIT--------------------------
# word=(input("enter the word: "))
# while word!='quit':
#     type=(input("enter the word: "))
   
# else:
#     print("successful")
# ----------------------------------------------cout how many digits-----------
# num=int(input("enter the number: "))
# digit=int(input("enter the digit: "))
# count=0
# while num>0:
#     l=num%10
#     if l==digit:
#         count+=1
#     num//=10                                               #remove last digit
# print(count)
# ------------------------------------------------------amstrong---------------------
# num=int(input("enter the number:"))
# og_num=num
# count=(len(str(num)))
# total=0
# while num>0:
#     l=num%10
#     total+=l**count
#     num//=10
# if total==og_num:   
#     print("its a amstrong number")    
# else:
#     print("its not an amstrong number")    
# -------------------------------------------------------DAY 1 TASK

# list_of_items=['tomato','potato','cucumber','onion','garlic']
# items_in_pantry=['chilly','cabbage','brinjal','tomato','potato']
# items_to_remove=[]
# items_to_purchare=[]
# for i in list_of_items:
#     if i in items_in_pantry:
#         items_to_remove.append(i)
#     if i not in items_in_pantry:
#         items_to_purchare.append(i)

# print("items to remove are:",items_to_remove)        
# print("items to purchare are:",items_to_purchare)

# -------------------------------------------------------------------sum of digits in a number
# a=int(input("enter the number:"))
# b=len(str(a))
# sum=0
# for i in range(0,b):
#     print("s")
#     d=a%10
#     sum+=d
#     a//=10
# print(sum)    
# ------------------------------------------------------------------------------------------

# num=int(input("enter the number: "))
# sum=0
# while num!=-1:
#      sum+=num
#      num=int(input("enter the number: "))
# print(sum)     
# ----------------------------------------------NESTED LOOP
# n=5
# for i in range(0,n):
#     for j in range(0,n):
    #     print("* ",end=" ")
    # print()    

# -------------------------------------------------------------1-25
# s=1
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print(s,end=" ")
#         s+=1
#     print()    
# ----------------------------------------------------------------------------------left angle increasing
# n=5
# b=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(b,end=" ")
#         b+=1
#     print() 
# ------------------------------------------------
 
# --------------------------------------------left side decreasing

# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print("* ",end=" ")
#     print() 

# ---------------------------------------------------------------------right side triangle increasing
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ") 
#     print()  
# --------------------------------------------------right side decreasing

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")    
       
#     print() 
# ------------------------------------------------pyramid
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("*",end=" ") 
#     for j in range(0,i+1):
#         print("*",end=" ")     

#     print()  

# --------------------------------------------reverse pyramid

# n=5
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")   
#     for j in range(i,n):
#         print("*",end=" ")    
#     print()    
# # -------------------------------------------------diamond
# n=5
# for i in range(0,n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("*",end=" ") 
#     for j in range(0,i+1):
#         print("*",end=" ")     

#     print()  
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")   
#     for j in range(i,n):
#         print("*",end=" ")     
#     print()    
# -----------------------------------------------------------hourglass
# n=5
# for i in range(0,n-1):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")   
#     for j in range(i,n):
#         print("*",end=" ")    
#     print()  

# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("*",end=" ") 
#     for j in range(0,i+1):
#         print("*",end=" ")     

    # print()  
# -----------------------------------------------------------1 to 10 in L increasing

# n=4
# b=1
# for i in range(0,n):
#     for j in range(i+1):
#         print(b,end=" ")
#         b+=1
#     print()    
# -----------------------------------------------------------------------------hollow  increasing triangle left
# n=5
# for i in range(n):
#     for j in range(i+1):
#         if i==(n-1) or j==0 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()    
# -----------------------------------------------------------hollow dcreasing triangle left

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==(n-1)-i: 
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")   
#     print() 

# ----------------------------------------------------------hollow square
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==0 or i==n-1 :
#             print("*", end="  ")
#         else:
#             print(" ", end="  ")
#     print()    

# -----------------------------------------------------------------hollow pyramid
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#          print(" ",end=" ")
#     for j in range(0,i):
#             if i==n-1 or j==0:
#                 print("*",end=" ") 
#             else:
#                 print(" ",end=" ")    
#     for j in range(0,i+1):
#         if i==n-1 or j==i:
#             print("*",end=" ")   
#         else:
#                 print(" ",end=" ")    


    # print()  
# ----------------------------------------------------------------------------hollow diamond
# n=5
# for i in range(0,n-1):
#     for j in range(i,n):
#          print(" ",end=" ")
#     for j in range(0,i):
#             if j==0:
#                 print("*",end=" ") 
#             else:
#                 print(" ",end=" ")    
#     for j in range(0,i+1):
#         if j==i:
#             print("*",end=" ")   
#         else:
#                 print(" ",end=" ")    
#     print()  

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         if j==i:
#             print("*",end=" ")   
#         else:
#             print(" ",end=" ")    
#     for j in range(n):
#         if j==(n-1)-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()    

# ---------------------------------------------------------------hollow reverse pyramid
# n=5
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         if i==0 or j==i:
#             print("*",end=" ")   
#         else:
#             print(" ",end=" ")    
#     for j in range(n):
#         if i==0 or j==(n-1)-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()    

# -----------------------------------------------------rhombus
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ") 
#     for j in range(i+1):
#         print("*",end=" ")   
       
#     print() 
# ----------------------------------------------------------pascals triangle
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("*",end=" ") 
#     for j in range(0,i+1):
#         print("*",end=" ")     

#     print()  


 

# ------------------------------------------------------task 2


# --------------------------------------------------------task3
# name=(input("enter your name: "))
# age=int(input("enter your age: "))
# print("hello,",name,"!You are",age,"years old.")

#  --------------------------------------------------------task4
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# if num1>num2:
#     num1+=10
# else:
#     num1-=5
# print("updated num1 =",num1)        
# ---------------------------------------------------------------task5
# name=(input("enter your name: "))
# age=int(input("enter your age: "))
# fav_num=int(input("enter your favorite number: "))
# print(f"hello {name} you are {age} years old and your favorite number is {fav_num}.")

# ---------------------------------------------------------------task8
# mark=int(input("enter your marks: "))
# if 95<=mark<=100:
#     print("congratulationss..!you have high distinction")
# elif 80<=mark<95:
#     print("your grade is A")

# elif 50<=mark<80:
#     print("your grade is B")   

# elif 0<=mark<50:
#     print("you are failed")     

# else:
#     print("invalid score")        

# -----------------------------------------------------------------------------------------task 8.2
# num=int(input("enter the number: "))
# if num>0:
#     print("its a positive number")
# elif num<0:
#     print("its negetive")   

# else:
#     print("its 0")    
#  ------------------------------------------------------------------------------------------task 9.1
# n=10
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum) 
# 
# -------------------------------------------------------------------------------------------------9.2
# num=[1,2,3,4,5,6]
# for i in num:
#     if i%2==0:
#         print(i)             
# ------------------------------------------------------------------------------------------------9.3 

# num=0
# for i in range(1,6):
#     for j in range(1,11):
#         num=i*j
#         print(i,"x",j ,"=",num)


# -----------------------------------------------------------------------------15
# food=["chocolates","ice cream","burger","pizza"]
# for i in food:
#     print("i love",i)
# ---------------------------------------------16.1
# num=[1,2,3,4,5,6,7,8,9,10]
# square=0
# for i in num:
#     square=i*i
#     print("square of",i,"is",square)
# -------------------------------------------------------16.2
# string="python programming is fun"
# vowels=("a","e","i","o","u")
# for i in string:
#     if i in vowels:
#         print(i)
# ------------------------------------------------16.3
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in list:
#     if i%2==0:
#         print(i)
# -----------------------------------------------17
# text="madam"
# print(text[0],text[-1])
# print(text[::-1])---------------------------------17.2
# text="madam"
# print(text.count('a'))--------------------------------17.3
# text=("python is easy to learn")
# print(text.replace(" ","_"))----------------------------17.4
# # text="madam"----------------------------------17.5
# reverse=text[::-1]
# if text==reverse:
#     print("its a palindrome")
# else:
#     print("its not palindrome")    

# -------------------------------------------------------------------18.1
# names=("safa","rumi","shamja","nami")
# grades=("A","B","C","A")
# students_grade=dict(zip(names,grades))
# print(students_grade)

# ---------------------------------------------ERRORRRR 18.2
# list1=[1,2,3,4]
# list2=[6,7,8,9]
# joined=list(zip(list1,list2))
# sum=0
# for i in joined:
    

# -------------------------------------------------unzip ERROOORRR 18.3

# zipped=[("safa",1),("nami",2),("kuromi",3)]
# names,num=list(zip(*names))
# print(unzip)


# ------------------------------------------------------19.1
# days=("monday","tuesday","wednesday","thursday","friday")
# # print(days[1])
# print(days.index("wednesday"))
# print(days[0:5])
# ------------------------------------------------------------------19.2

# names=["safa","navami","siraj","safa","siraj"]
# unique_names=set(names)
# print(unique_names)

# -------------------------------19.2 sub
# a={1,2,3,4,5,6}
# b={3,4,5}
# # print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# if a>b:
#     print("a is the superset of b")
# elif a<b:
#     print("a is subset of b")

# else:
#     print("a is equivalent to b")    

# -------------------------------------------------fibanocci pattern
# n=int(input("enter the number:"))
# a=0
# b=1


# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         c=n-j
#         print(c,end=" ")



#     for j in range(i,n):
#         c=i+j
#         print(c,end=" ")     
       
#     print() 
# ------------------------------------------------------------------------electricity bill
# print("ELECTRICITY BILL SYSTEM")
# n=int(input("Enter the units: "))
# if 0<=n<100:
#     print("amount:",5*n)
# elif 100<=n<200:
#     print("amount:",(100*5)+((n-100)*8))
# elif 200<=n<300:
#     print("amount:",((100*5)+(100*8)+((n-200)*10)))      
# else:
#     print("amount:",((100*5)+(100*8)+((n-200)*10)))   
#  -----------------------------------------------------------------------   
 
































# -------------------------------------------fibanocci
# a=int(input("fibanocci series..:"))
# b=0
# c=1
# d=0
# z=[]
# z.append(b)
# z.append(c)
# for i in range(1,a-1):
#     d=b+c
#     b=c
#     c=d
#     z.append(d)
# print(z)    