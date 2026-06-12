# What is function in python
#1. Every  function has their own purpose.
#2. Function is  block of instruction(code) which excute inside its own block.
#3. function is reuseable means define one time use manytime(DRY-don't repeat yourself)
#4. function has two main part first functions defination second function calling.

# how define function in python.

# def add():
#     a = 10
#     b= 20
#     c = a+b
#     print(c)

# add() # function call

# function divide into four category.
#1. Take nothing return nothing.
#2. Take nothing return something.
#3. Take something return nothing.
#4. Take something return someting.

# Parameters(para) and arguments(args).
# Positional parameter/arguments


# def add(a,b):
#     c = a+b
#     print(c)
# add(30,50) # we call functions multiple time 

# def table_print(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")
# table_print(5)
# print("-"*20)
# table_print(19)
# print("-"*20)
# table_print(2)

# # default parameter
# def add(a=0,b=0):
#     print(a+b)
# add(1,1)

# #add function
# def add(a,b):
#     c = a+b
#     print("Addition",c)


# #subtract function
# def sub(a,b):
#     c = a-b
#     print("Subtaction",c)


# #multiplication function
# def multi(a,b):
#     c = a*b
#     print("Multiplication", c)


# #divide function
# def div(a,b):
#     c = a/b
#     print("Division",c)

# while True:
#     a = int(input("Enter number 1 :"))
#     b = int(input("Enter number 2 :"))
#     option = input("chose the option : +, -, *, / (0: for stop program) : ")
#     if option == "0":
#         print("Program closed")
#         break
#     elif option == "+":
#         add(a,b)
#     elif option == "-":
#         sub(a,b)
#     elif option == "*":
#         multi(a,b)
#     elif option == "/":
#         div(a,b)
#     else:
#         print("chose write option :")


# def add(a,b):
#     c = a+b
#     return c
# res = add(2,3)
# print(res)

# def add(a,b):
#     return a+b
# res = add(2,3)
# print(res)

# def sub(a,c):
#     return a-c
# print(sub(10,res))

# def greet(a):
#     return a
# res = greet("hello")
# def user_name(a):
#     return a
# res1=user_name("Dev")
# print(greet(res), user_name(res1))

# #another way
# def greet(a):
#     return a
# def user_name(a):
#     return a
# print(greet("hello"), user_name("Aman"))


#wap to check number pass by argument is odd aor even
# num1 = int(input("Enter a number : "))
# def Check_number(num1):
#     if num1 %2 == 0:
#         print("Number is Even ! ")
#     else:
#         print("Number is odd ! ")

# Check_number(num1)

#waf to check which number is greater and two number by user
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# def Check_number(num1,num2):
#     if num1 > num2:
#         print(f"{num1} is greater than {num2} ! ")
#     elif num2 > num1:
#         print(f"{num2} is greater  than {num1}! ")

# Check_number(num1,num2)

#waf to check the character pass by user is volwel or constonant

# def check_vowel_consonant(char):
#     if char in "aeiouAEIOU":
#         print("It's Vowel")
#     else:
#         print("It's consonant")
# char = input("Enter a Character : ")
# check_vowel_consonant(char)

#waf to check is number completely divide by 2 and 3 and return 

# def check_division(number):
#     if number % 2 == 0 and number % 3 == 0:
#         return "Yes number is completely divide"
        
#     else:
#         return "No number is not Completely divide"
        
    
# number = int(input("Enter a number : "))
# res = check_division(number)
# print(res)

#waf to retrun lenght of a string pass user without using len():

def lenght_string(str1):
    print(str1)
    c = 0
    sum = 0
    for i in str1:
        c += 1
        sum = i + sum
    print(sum)
    return c

str1 = input("Enter a string : ")
res = lenght_string(str1)
print(sum)
print(res)

#waf to check given how many vowels in given string

# string = input("Enter A String : ")

# def vowel_count(string):
#     count = 0
#     for i in string:
#         if i in "aeiouAEIOU":
#             count += 1
    
#     return count

# res = vowel_count(string)
# print(res)

#local variable vs global varialbe

# def masg():
#     global name # here we define name golbal variable with use keyword local for access outside from function
#     name = "Shekhar"
#     print(name)

# masg()
# print(name)


#waf to count char "p" in "Python Programing" return total occurence
string = "python programing "
# def count_char(string):
#     count = 0
#     for i in string:
#         if i == "i": # if we check one char in string so we use comparision operator but 
#                      #we check a string in string so we use in operator
#             count += 1
#     return count

# res = count_char(string)
# print("  char in String : ",res)


#waf to return sum of string indexes:

# str = "Python"
# def String_sum(str):
#     sum = 0
#     for i in range(len(str)):
#         sum = sum + i
#     return sum
# res = String_sum(str)
# print(res)
