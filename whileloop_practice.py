# #wap to count all vowels from give string: "this is devops batch"
# str1 = "this is devops batch"
# vowels = "aeiouAEIOU"
# count = 0
# i=0
# while i < len(str1):
#     if str1[i] in vowels:
#         count += 1
#     i += 1
# print(count)

# # wap to print your name in reverse format:
# Name = "Shekhar"
# reverse = ""
# i=0
# while i < len(Name):
#     reverse =Name[i] + reverse 
#     i += 1
# print(reverse)

# #Wap a program to print like this
# # P PYTHON 0
# # Y PYTHON 1
# # T PYTHON 2
# # H PYTHON 3
# # O PYTHON 4
# # N PYTHON 5

# Name = "PYTHON"
# i = 0
# while i < len(Name):
#     print(Name[i],Name, i)
#     i += 1

# #wap to sum of the indices of string : "python"

# string = "python"
# i = 0
# sum = 0
# while i < len(string):
#     sum = i + sum
#     i += 1
# print(sum)

# #wap to print the factorial from 1 to 9

# i = 1
# factorial = 1
# while i <= 9:
#     factorial = factorial* i
    
#     print(i,"!=",factorial)
#     i += 1


# #wap to print only prime number from 1 to 15
# num=1
# while num <= 15:
#     if num > 1:
        
#         i=2
#         while i <num:
#             if num %i ==0:
#                 break
#             i += 1

#         else:
#             print(num)
#     num += 1


# #1. wap to takes start_point and end_point from user input and print all number divisble by 2 and 3

# start_point = int(input("Enter Start Point :"))
# end_point = int(input("Enter end Point :"))

# while start_point <= end_point:
#     if start_point %2 == 0:
#         print(f"Number Divisble by 2 : {start_point}")
#     if start_point % 3 == 0:
#         print(f"Number divisble by 3: {start_point}")
#     start_point += 1


#wap to print all the total of even number from 1 to 15

# sum=0
# i=2
# while i <= 15:
#     if i % 2 ==0:
#         sum = i+sum
#         print(i)
#     i += 1
# print(f"sum of even number :{sum}")

# #wap to check the give string by user is "palidrome " or "not palidrome"

# str1 = input("Enter the string : ")
# reverse = ""
# i = 0
# while i < len(str1):
#     reverse =str1[i] + reverse 
#     i += 1
# if str1 == reverse:
#     print("string is palidrome : ")
# else:
#     print("string is not palidrome")
    

# text = input("enter the text: ")
# copy_text = text








#wap to reverse the digit : 1234 , output : 4321

num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)
    