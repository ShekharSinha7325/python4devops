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

def greet(a):
    return a
res = greet("hello")
def user_name(a):
    return a
res1=user_name("Dev")
print(greet(res), user_name(res1))

#another way
def greet(a):
    return a
def user_name(a):
    return a
print(greet("hello"), user_name("Aman"))

