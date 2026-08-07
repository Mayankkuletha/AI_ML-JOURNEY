# POLYMORPHISM method 

#Inheritance --> an object could be treated as the same type as a parent class
# Python ki ek library se hum do cheezein import kar rahe hain:

# ABC
# abstractmethod
# ABC

# ABC ka matlab:

# Abstract Base Class

# Humari parent class ko abstract banane mein help karta hai.
from abc import ABC,abstractmethod
class Shape():
    # Abstract method ka simple meaning:

# Parent class mein method ka rule define karo, but actual implementation child classes par chhod do.
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class Pizza (Circle):

    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4) , Square(5) , Pizza("pepperoni",15)]

for shape in shapes:
    print(f"{shape.area()}.cm2")



