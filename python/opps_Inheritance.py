# example:A dog inheritsnce from an animal

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("dog Barks")
# dog=Dog()
# dog.speak()



class A:
    a=12
class B(A):
    b=22
# to 2 lines are comes under single level Inheritance
class C(B):
    c=33
# when ever adding another line its called multi level Inheritance
obj=C()
print(obj.a)
print(obj.b)
print(obj.c)      


# Hirarical In heritance Type

class A:
    a=12
class B:
    b=22
class C(A,B):
    c=33

obj=C()
# print(obj.a)
# print(obj.c)
print(obj.b)