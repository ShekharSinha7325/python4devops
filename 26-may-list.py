#data structure
#data structure used to store data effeciently and work faster
#for operation like read and write

#list : list[]
#string : str " " or 
#dictonary : dict{}
#set : set{}
#tuple : tuple()



#######################** list **#######################################
#1. list is a data structure  in python used to store multiple dta of  diffrent types in one variable
#2. kist can define by using square[] and data inside known as a element.
#3. list can be  hetrogenous and homogenous,
#4. list are mutable (changeable).
#5. list support indexing , slicing, and follows ordering sequence.

#1.creation of list
#2.updation of list
#3.indexing
#4.slicing
#5.Traversing
#6.In-built methods
#7.Test
#8.Assignment




# # total index = length -1
# marks_10th = [20,55,60,76,50,60,"hello", 5.5 ]
# #print("before update :", marks_10th)
# #marks_10th[0] = 200 #muating list element using index.
# # marks_10th[-1] = 200
# i = marks_10th[0]
# print(marks_10th[i])
# #print("after update :", marks_10th)

#4.slicing
# marks = [10,20,30,40,50,60,70,80]
# # [start-0:stop-1:step-1]
# # sub_list = marks[2:6]
# # sub_list = marks[0:8:2]
# sub_list = marks[::-1]
# print(sub_list)

#5.Traversing
# marks = [10,20,31,30,40,43,50,60,67,70,80,101]
# for i in range(len(marks)):
    # print(i)
    # print(marks[i],end=" ")
    # if marks[i] % 2 == 0:
    #     print(marks[i],end=" ")
    # if marks[i] % 2 != 0:
    #     print(marks[i],end=" ")

# marks = [10,20,31,30,40,43,50,60,67,70,80,101]
# total = 0
# for i in marks:
#     total = total + i
# print("Total sum of elemets : ",total)

marks = [10,20,30,40,50,60,70,80,90,100]
# sub_list = marks[2:9]
# sub_list = marks[:7]
# sub_list = marks[:-3]
#sub_list = marks[:-4:-3]
# sub_list = marks[2:0:-1]
sub_list = marks[::-1]
# print(sub_list)

#wap to swap first and last value of list
# marks = [10,11,20,31,30,33,40,55,50,60,70,80]
# print("befor swaping the list")
# print(marks)
# result = marks[0]
# marks[0]= marks[-1]
# marks[-1]=result
# print("After swaping a list")
# print(marks)

# for i in range(len(marks)):
#     if marks[0] == marks[-1]:

# my_list = [10,20,30,40]
# sum = 0
# for i in range(len(my_list)):
#     sum = 
# my_list[i] + sum
# print(sum)




#wap  to find the  sum of only even elemnts of list my_list = [10,20,30,40]
# my_list = [10,20,30,40]
# sum = 0
# for i in range(len(my_list)):
#     if my_list[i] % 2 == 0:
#          sum = my_list[i] + sum
# print("Sum of all even number",sum)

#wap  to find the  sum of only odd elemnt of listmy_list = [10,20,30,40]
# my_list = [10,20,30,40]
# sum = 0
# for i in range(len(my_list)):
#     if my_list[i] % 2 != 0:
#          sum = my_list[i] + sum
# print("Sum of all even number",sum)


#wap  to  find the count how many int value and how many string value in list 
# my_list =  [70,"aman",50,10,20,"rohan", "iq-india"]
# my_list = [70,"aman",50,10,20,"rohan", "iq-india"]
# int_count = 0
# str_count = 0
# for i in my_list:

#     if type(i)==str:
#         str_count += 1
#     elif type(i) == int:
#         int_count += 1

# print("String Count is : ", str_count)
# print("Int Count is :", int_count)


#7 In-built methods.
#append() : elements add to last  index.
# emp_name = ["aman","shivam"]
# new_emp = "Kamal"
# print(emp_name)

# emp_name.append(new_emp)
# print(emp_name)

# new_emp1 = "rohan"
# emp_name.append(new_emp1)
# print(emp_name)

# emp_name = ["aman","shivam"]
# print(emp_name)
# emp_name.append(["name", 67,True,False,"Noida"])
# print(emp_name[2][0])

#extend():its extend the value of list nested loop make one list and its add multiple value at one time
#  

emp_name = ["aman","shivam"]
print(emp_name)
emp_name.extend(["name", 67,True,False,"Noida"])
print(emp_name[2][0])

#insert(position,value)
emp_name = ["aman","shivam"]
print(emp_name)
emp_name.insert(1,"Iq-india")
print(emp_name)

#pop():default delete and return from last otherwise specific 
my_list=[100,200,300,400,500,600,700]
d1=my_list.pop()
print(my_list)
print("Deleted Elements : ", d1)

#remove 
my_list=[100,200,300,400,500,600,700]
r1=my_list.remove(200)
print(my_list)
print("Deleted Elements : ", r1)

#reverse
my_list=[100,200,300,400,500,600,700]
r1=my_list.reverse()
print(my_list)

#sort()
my_list=[100,200,300,400,500,600,700]
# r1=my_list.sort()
r1=my_list.sort(reverse=True)
print(my_list)

#copy()
my_list=[100,200,300,400,500,600,700]
dup_list=my_list.copy()
print(my_list)
dup_list.pop(3)
print(dup_list)

#count()
my_list=[100,200,300,400,500,600,700]
res=my_list.count(100)
print(res)

#universal..
my_list=[100,200,300,400,500,600,700]
print(sum(my_list))
print(min(my_list))
print(max(my_list))