a= lambda x,y,z:x+y+z
print("ADDITION", a(2,4,6))

a= lambda x,y,z:x-y-z
print("substraction", a(2,4,6))

a= lambda x,y,z:x*y*z
print("Multiplication", a(2,4,6))

a= lambda x,y,z:x/y/z
print("division", a(2,4,6))


# Write a Python program to sort tuples using Lambda.
a=[1,4,0,5,3]
b=list(a)
c=sorted(b,key=lambda x:x)
print("sorted",c)


# Write a Python program to square and cube every number in a given list of integers using Lambda

a=[1,2,3,4]

square=list(map(lambda x:x**2,a))
print(square)

cube=list(map(lambda x:x**3,a))
print(cube)

# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.

a=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,a))
print(even)

# Write a Python program to add two given lists using map and lambda.

m=[1,2,3,4,5,6,7,8,9]
l=[9,8,7,6,5,4,3,2,1]

s=list(map(lambda x,y:x+y,m,l))
print(s)