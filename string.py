#string("", '', """ """, ''' ''') :- A string is just text (sequence of characters)
#var1 = "d"

student_name = "Amna Kumar"
student_address = "D-1 255/455 NOIDA SEC-15 NEW  DELHI 110096"
student_number = "7634958565"
#print(len(student_number))
student_profile = f"""Hello, Myself {student_name} and
 i am devops inter looking 
 for some challenging opertu....  my adress {student_address}  contact {student_number}"""

#print(student_profile)


#operators in Python
# 1. Airthmatic opr
# 2. Assignment opr
# 3. comprasion/ relational opr
# 4. logical opr
# 5. membership opr
# 6. identity opr
# 7. bitwise opr

# 2. Assignment operator
a=10
#a= a+10 # standard way
a+= 10 # shorthand method
a*= 10 # shorthand method
#print(a)

# 3. comprasion/ relational opr(>,<,>=,<=,==,!=)
n1 = 30
n2 = 40
#print(n1>n2)

#>,<,>=,<=,==,!= self assesment 

str1 = "A"
str2 = "a"
#print(str1>str2)

# 4. logical opr
n1 = 1
n2 = 3
res = n1 ==1 and n2 == 3 and n1 == 2 and n2 == 3
print(res)
res = n1 ==1 or n2 == 3 or n1 == 2 or n2 == 3
print(res)
res = not(n1 ==1 or n2 == 3 or n1 == 2 or n2 == 3)
print(res)
