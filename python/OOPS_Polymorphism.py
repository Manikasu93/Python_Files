# Ex:Different animals making Different Sounds 
#When Ever Having same Nmaes are Notting but Method Overloading

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

animals=[Cat(),Dog()]

for animal in animals:
    animal.speak() # Different Behaviour Based On Object Type






