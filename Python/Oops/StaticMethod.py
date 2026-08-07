# Static methods -- > A method that belong to a class rather than any object from that class instance usually used for general utility functions

# Instance methods --> Best for operations on Instances of the class (objects)
# Static methods --> best for utility functions that do not need acess to class data

class Employee :

    def __init__(self,name , position):
        self.name = name
        self.position = position
    # Instance method means ki for every object value may change.
    def get_info(self):
            return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
         valid_positions=["Manager","Cook" , "Cashier","Janitor"]
         return position in valid_positions

emp1=Employee("mayank","Manager")
emp2=Employee("himanshu","Cook")
emp3=Employee("Karan ", "Janitor")

# we can acess them directly using class.
print(Employee.is_valid_position("Cook"))
# we have to access instance variables like this.
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())