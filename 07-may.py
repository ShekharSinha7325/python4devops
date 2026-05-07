# neated if else (chaining, ladder)
# name = ""
# if name:
#     #print("Yes Name is provided")
#     print(f"Yes Name {name}  is provided")
#     address = "Noida"
#     if address:
#         print(f"Yes address is : {address} provided")
#     else:
#         print(f"Yes address is not : {address} provided")
# else:
#     print("Name is not provided")

# num1 = 20
# if num1 % 2 ==0:
#     print("Even")
#     mob = input("Enter your MOb no : ")
#     print(mob)
#     if len(mob) == 10: 
#         print("Valid Number")
#     else:
#         print("Invaid number")
# else:
#     print("Odd")


student_name = input("Enter Your Name : ")
pre = int(input("Enter your pre marks : "))
if pre >=400:
    print("Your pre is qualified you are eligible for Mains")
    mains = int(input("Enter your Mains Marks :"))
    if mains >= 600:
        print("You are pass in mains and eligible for Interview ")
        interview_marks = int(input("Enter your Interview Marks :"))
        if interview_marks >= 100:
            print(f"Your are slected as IAS mr. {student_name}")
        else:
            print(f"Your Failed In Interview mr.{student_name} ")
    else:
        print("Better Luck next time❕, Mains failed ❌")
   
else:
    print("Better luck next time , pre failed ❌")