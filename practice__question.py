#1. wap to takes start_point and end_point from user input and print all number divisble by 2 and 3
# start_point = int(input("Enter start Point : "))
# end_point = int(input("Enter end Point : "))

# for i in range(start_point,end_point):
#     if i%2 == 0:
#         print(f"Number Divisble by 2 : {i}")
#     if i %3 == 0:
#         print(f"Number divisble by 3 : {i}")



#Another Way if you want print seprate divisble by 2 and divisble by 3
# start_point = int(input("Enter start Point : "))
# end_point = int(input("Enter end Point : "))

# print("Numbers Divisible by 2")

# for i in range(start_point, end_point + 1):
#     if i % 2 == 0:
#         print(i)

# print("Numbers Divisible by 3")

# for i in range(start_point, end_point + 1):
#     if i % 3 == 0:
#         print(i)
   


#2. wap to take a number from user input and print formated table
# formate
# 3x1=3
# 3x2=6
# ....
# 3x10 = 30

# Num = int(input("Enter a number : "))
# for i in range(1,11):
#     n1 = Num*i
#     print(f"{Num} X {i} : {n1}")

 


#3. wap to take a number from user input and print  reverse formated table
# formate
# 3x10=30
# 3x9=27
# ....
# 3x1 = 3

# Num = int(input("Enter a number : "))
# for i in range(10,0,-1):
#     n1 = Num*i
#     print(f"{Num} X {i} : {n1}")


#pattern Program

# n = 7
# for i  in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1 or i == n//2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    

#wap to check odd_even
def odd_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

res = odd_even(10)
print(res)
    
