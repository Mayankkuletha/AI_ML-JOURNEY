# multiple inheritance = inherit from more than one parent class
# C(A,B)

# Multilevel inheritance = inherit from a parent which inherits from another parent
# C(A,B) <- B(A) <-A 

class Animal:
    def __init__(self,name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} can fley")

class Predators(Animal):
    def hunt(self):
        print(f"{self.name} can hunt")

class Rabbit(Prey):
    pass

class Hawk(Predators):
    pass

class Fish(Prey,Predators):
   pass

rabbit = Rabbit("bugs")
hawk = Hawk("tony")
fish = Fish("machli")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.sleep() #Animal.sleep(fish)Internally so we have to pass sleep