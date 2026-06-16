# a=4
# if a>=5:
#     print("A is grater than or equal to 5")
# else:
#     print("A is Not grater than or equal to 5")


#WAP to check the eligibility criteria for voting 
# age=int(input("enter your age:"))
# if age>=21:
#     print("Your are eligible for voting")
# elif age>=18 and age<=21:
#     print("Your are eligible but not to partisipate")
# else:
#     print("Your are not eligible for voting")

# ________________________________________________________________________________________________________

#WAP to find greatest of 3 numbers a=10,b=27,c=6.
# a=10
# b=27
# c=6
# if a>=b and b>=c:
#     print(a, "a is greatest")
# elif a>=c:
#     print(b,"b is greatest")
# else:
#     print(c,"c is greatest")


# # WAP to check whether 10 is divisible in both 2 and 4.

# a=10
# if a%2==0 and a%4==0:
#     print(a,"a is Divisiable")
# else:
#     print("It Was not divisiable")

# # WAP to check whether 8 is divisible in either 3 or 4.

# a=8
# if a%3==0 and a%4==0:
#     print(a,"a is divisiable")
# else:
#     print("It Was not divisiable") 

# # WAP to print Grades:
# # Grade A: if marks is beteween 76 and 100
# # Grade B: if marks is beteween  51 and 75
# # Grade C: if marks is beteween 26 and 50
# # Grade D: if marks is beteween 0 and 25

# a=int(input("Enter Number:"))
# if a>=76 and a>=100:
#     print("Grade:A")
# elif a>=51 and a>=75:
#     print("Grade:B")
# elif a>=26 and a>=50:
#     print("Grade:")
# else:
#     print("Fali")

# # Write a Python program to check if a number is positive, negative, or zero.

# a = int(input("enter the number:"))     
# if a==0:
#     print(a,"A is Zero")
# elif a > 0:
#     print("A Is Positive")
# else:
#     print("A Is negitive")



# # Write a Python code to check if a number is even or odd

# a=int(input("enter the number:"))
# if a%2==0:
#     print("entered number Is Even")
# else:
#     print("entered Number is Odd")

# # Write a Python program to find the maximum of three numbers
a1=int(input("enter the first number:"))
a2=int(input("enter the second  number:"))
a3=int(input("enter the third number:"))

if a1>a2 and a1>a3:
    print("The Maximum number is",a1)
elif a2>a1  and a2>a3:
    print("The Maximum number is",a2)
else:
    print("The Maximum number is",a3)