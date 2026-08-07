class Car : 
    # Constructor 
    def __init__(self , model , year , color , for_sale):
        self.model = model
        self.year = year 
        self.color = color 
        self.for_sale = for_sale

# car1= Car("Mustang",2024,"red",False)
# print(car1.model)

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You Stop the {self.color}{self.model}")

    def describe(self):
        print(f"{self.year}{self.color}{self.model}")