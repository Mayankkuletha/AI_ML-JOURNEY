# Super --> Function used in a child class to call methods from a parent class(superClass).
# Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self,color,is_filled, radius):
        super().__init__(color , is_filled)
        self.radius = radius
    def describe(self):
            super().describe()
            print(f"It is a circle of area {3.14*self.radius*self.radius} cm^2 ")
        

class Square(Shape):
    def __init__(self,color , is_filled, width):

        super().__init__(color,is_filled)
        self.width = width

       
class Triangle(Shape):
    def __init__(self,color ,is_filled,height):
        super().__init__(color,is_filled)
        self.height = height

circle = Circle("Red" , True , 5)
square = Square("Green",False,8)
triangle = Triangle("red",True,8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe() #function under child will get priority rather than parent if name of function is same


