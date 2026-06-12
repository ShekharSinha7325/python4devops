emp_list = []
for i in range(1,11):
    emp_list.append(i)
print(emp_list)

my_list = [i for i in range (1,11)]
print(my_list)
my_list = [i**2 for i in range (1,11)]
print(my_list)
my_list = [i if i%2 == 0 else "" for i in range (1,11)]

print(my_list)
my_list = [i for i in range (1,11) if i%2 == 0]
print(my_list)
my_list = [str(i)+':even' if i%2 == 0 else str(i)+':odd' for i in range (1,11)]
print(my_list)

emp_name=["aman","SHIVAM","Rahul"]
res = [n.lower() for n in emp_name]
print(res)
res = [n.upper() for n in emp_name]
print(res)
res = ["-".join(n) for n in emp_name]
print(res)

fruit_list = ["apple","mango","papaya","banana","orange","grapes"]


user_input = input("Enter a character ")
# through list-comprehension
res = [i.upper() for i in fruit_list if user_input in i]
print(res)
# through normal-way
for i in fruit_list:
    if user_input in i:
        print([i],end=" ")   