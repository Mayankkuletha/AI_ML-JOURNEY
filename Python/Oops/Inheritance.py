#Inheritance --> Allows a class to inherit attributes and methods from another class.
# Helps with code reuablity and Extensiblity
# class Child(Parent)

class Animal :
    def __init__(self,name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
            print("MEOW")
    

class Mouse(Animal):
    def sound(self):
            print("CHUHUCHU")
    

dog = Dog("Scooby")
# self = dog
# name = "Scooby" internally aisa ho jata hai
cat = Cat("Smoky")
mouse = Mouse("Mickey")
print(dog.name)
print(cat.name)
print(mouse.name)
print(dog.sleep())
print(cat.eat())
print(cat.sound())