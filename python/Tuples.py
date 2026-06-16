#Tuples cannot be sorted because it is a immutables

# Exercise 1: Basic Tuple Operations

# a=(1,2,3,"mani")
# print(len(a))
# print(a[3])
# print(a[1])
# print(a[::-1])
# Exercise 2: The Trailing Comma
a=(5,)
print(type(a))


# Exercise 3: Tuple Repetition
a=(1,2,3,"mani",6,8)
print(a*4)

# Exercise 4: Tuple Concatenation
a=(1,2,3,"mani",6,8)
b=(1,2,3,"kasu",6,8)
print(a+b)

# Exercise 5: Tuple Slicing
a=(1,2,3,"mani",6,8)
print(a[1:5])

# Exercise 6: Tuple Reversal
a=(1,2,3,"mani",6,8)
print(a[::-1])
# Exercise 7: Counting
a=(1,2,3,"mani",66,88)
b=a.count(66)

# Exercise 8: Tuple Unpacking
a=(1,2,3,"mani",77)
b,c,d,e,f=a
print(b,c,d,e,f)

# Exercise 9: The Swap Trick
a=(1,2,3,"mani",6,8)
b=a=(1,2,3,"mani")
c,d=a,b
# Exercise 10: Nested Tuple Access
a=((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(a[0][1])
print(a[1][2])
print(a[2][1])