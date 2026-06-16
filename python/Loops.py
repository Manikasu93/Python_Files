# 1. For Loop

# Syntax:
# for var in range(5):#------->0,1,2,3,4
#   print("Uncodemy")

# for var in range(1,11):
#   print(var)

# for var in collections:
#   print(var)
# for i in  range(11):
#   print(i,end=" ")
  
  
       #Exercises#
# Exercise 1: Print first 10 natural numbers using for loop
# Exercise 2: Calculate sum of all numbers from 1 to a given number
# Exercise 3: Print multiplication table of a given number
# Exercise 4: Count the total number of digits in a number
# Exercise 5: Display numbers from -10 to -1 using for loop
# Exercise 6: Display a message “Done” after the successful execution of the for loop


# for i in range(1,11):
#   print ("Natural number:",i )

# Exercise 2: Calculate sum of all numbers from 1 to a given number

# a=int(input("Enter the Number: "))
# sum=0
# for i in range(1,a+1):
#     sum+=i
#     print(sum)

# Exercise 3: Print multiplication table of a given number
# a=int(input("enter the number: "))
# mul=0
# for i in range(1,11):
#     mul= i * a
#     print(a,"X",i,"=",mul)


# Exercise 4: Count the total number of digits in a number
# a=str(12345)
# count=0
# for i in a:
#     count+=1
#     print(i)


    # Exercise 5: Display numbers from -10 to -1 using for loop
# for i in range(-10,0):
#     print(i,end=" ")


# Exercise 6: Display a message “Done” after the successful execution of the for loop
# print("Done")

                                    # While_LOOP

# c=1
# while c<=5:
#     print("course")
#     c=c+1



# Exercise 1: Print first 10 natural numbers using while loop
# c=1
# while (c<10):
#     print(c)
#     c+=1



# Exercise 2: Calculate sum of all numbers from 1 to a given number

# a=1
# sum=0
# n=int(input("Enter the Number: "))
# while a<=n:
#     sum+=a
#     a+=1
#     print(sum)



# Exercise 3: Print multiplication table of a given number
# a=1
# n=int(input("Enter the Number: "))
# while a <= 10:
#     mul=n*a
#     print(mul)
#     a+=1

# mul=0
# for i in range(1,11):
#     mul= i * a
#     print(a,"X",i,"=",mul)


# Exercise 4: Display numbers from a string using a loop

text = "abc123xyz"

for i in text:
    if i.isdigit():
        print(i)

# Exercise 5: Count the total number of digits in a number
digits="12345"
l=len(str(digits))
print(l)