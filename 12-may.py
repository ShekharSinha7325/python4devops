# traversing of string using range
# name = "python"
# size = len(name)
# for i in range(size):   # for i range(len(name))
#     print(name[i], end="")


# #without using range
# name = "Python Programing"
# for i in name:
#     print(i, end="")


# for i in "python":
#     print(i, end="")


# var1 = "Devops Engineer"
# for i in var1:
#     if i == 'e':
#         continue
#     print(i,end="")

#wap to count all vowels from give string: "this is devops batch"

# var1 = "this is devops batch"
# v_count = 0
# c_count = 0
# for i in var1:
#     if i in "aeiouAEIOU":
#         v_count += 1
#     else:
#         c_count += 1
    
# print(f"Vowel :{v_count}")
# print(f"Contonant : {c_count}")


# wap to print your name in reverse format:

# Name = "Shekhar"
# reverse = ""
# for i in Name:
#     reverse = i + reverse
#     # " " = S + " "
#     # "S" = h + " S"
#     # "hS" = e + "hS"
#     # "ehS" = k + "ehS"
#     # "kehS" = h + "kehS"
#     # "hkehS" = a + "hkehS"
#     # "ahkehS" = r + "ahkehS"
#     # "rahkehS" = 
# print(reverse)

#Wap a program to print like this
# P PYTHON 0
# Y PYTHON 1
# T PYTHON 2
# H PYTHON 3
# O PYTHON 4
# N PYTHON 5
# name = "PYTHON"
# size = len(name)
# for i in range(size):   
#     print(name[i],name,i)

     
#wap to sum of the indices of string : "python"

name = "python"
sum = 0
for i in range(len(name)):
    sum = sum + i
print(sum)

#wap to print the factorial from 1 to 9

factorial = 1
for i in range(1,9):
    factorial = factorial*i
    print(i, "!= " ,factorial)


#wap to print only prime number from 1 to 15

for num in range(1,16):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)

