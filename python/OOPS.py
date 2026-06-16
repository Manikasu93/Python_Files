# class A:
#     m=33              #Normal  Variable 
#     def m1(self):
#         print("mani")
# obj=A()       #Instance 
# print(obj.m)
# obj.m1()
# print(A.m)

# example:Car_Class(BluePrint)

class car:    #Class Attribute (Shared By All Cars)
    wheels=4

    #constructor (Used to create objects)
    def __init__(self,brand ,model):
       
       self.brand=brand #instance Attribute
       self.model=model #Instance Attribute


#Method(Action)
    def display_info(self):
        print(f'{self.brand} {self.model} {self.wheels} Wheels')

obj=car("skoda","2025")
obj.display_info()