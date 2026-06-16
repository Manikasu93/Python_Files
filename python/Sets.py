# Exercise 1: Basic Set Operations

a1={12,12.5,12.5,"Mani","Uncodemy",True}
print(a1)
a1.add("suresh")
print(a1)


# Exercise 2: Clear All Elements
a1={12,12.5,12.5,"Mani","Uncodemy",True}
a1.clear()
print(a1)
# Exercise 3: Find the Length of a Set
a1={12,12.5,12.5,"Mani","Uncodemy",True}
print(len(a1))

# Exercise 4: Check if a Set is Empty
a1={12,12.5,12.5,"Mani","Uncodemy",True}
if len (a1)==0:
    print("set is not empty")
else:
    print("set is empty")


# Exercise 5: Union of Sets
a1={1,23,4}
a2={4,3,3,6}
union_set=a1|a2
print(union_set)

# Exercise 6: Intersection of Sets
a1={12,12.5,2,5,5,"Mani","Uncodemy",True}
a2={12,5,5,5}
c=a1.intersection(a2)
print(c)
# Exercise 7: Difference of Sets
a1={12,12.5,2,5,5,"Mani","Uncodemy",True}
a2={12,5,5,5}
c=a1.difference(a2)
print(c)

# Exercise 8: Symmetric Difference
a1={12,12.5,2,5,5,"Mani","Uncodemy",True}
a2={12,5,5,5}
c=a1.symmetric_difference(a2)
print(c)

# Exercise 9: Find Max and Min
a1={12,12.5,2,5,5,True}
print(max(a1))
print(max(a1))

# Exercise 10: Sum of Set Elements
print(sum(a2))

# Exercise 11: Add a List of Elements
a1={1,2,3,4}
a2={5,6,7,3}
c=a1.update(a2)
print(a1)