# 6. identity opr (is , is not)

# a = 1000
# b = 1000
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)

#conditional statement

# a = 0
# if a:
#     print("yes")
# else:
#     print("no")


# if True:
#     print("yes")
# else:
#     print("no")


# a = True
# b = True
# print(a+b)

# write a progragram(wap) to check number give user in odd or even

# #num = 23
# num = input("Enter the Number :")
# if num % 2 ==0:
#     print("Even Number")
# else:
#     print("Odd Number")

# wap to print the last digit of a number is 456735

# num = "456735"
# print(num[-1])

# number = 456735
# last_digit = number % 10
# last_digit = number % 100
# print(last_digit)

#wap to find largest and  smallest number
#first Approach :-
# num1 = 3
# num2 = 9
# num3 = 12
# # largest_number = max(num1, num2 , num3)
# # Smallest_number = min(num1, num2 , num3)

# # print("Largest Number is  : ", largest_number)
# # print("Smallest Number is : ", Smallest_number)

# #second Method :-
# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is greatest")
# if num2 >= num1 and num2 >= num3:
#     print(f"{num2} is greatest")
# if num3 >= num1 and num3 >= num2:
#     print(f"{num3} is greatest")

# if num1 <= num2 and num1 <= num3:
#     print(f"{num1} is smallest")
# if num2 <= num1 and num2 <= num3:
#     print(f"{num2} is smallest")
# if num3 <= num1 and num3 <= num2:
#     print(f"{num3} is smallest")

# multiple if condition
n = 100
if n>50:
    print("Yes1")
if n>60:
    print("Yes2")
if n>70:
    print("Yes")
else:
    print("No")   #if multiple if condition and last
                  # me else statement h to oo apne se uper wale if ko trigger krega baki ko nhi
