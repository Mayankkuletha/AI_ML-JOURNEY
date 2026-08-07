# Class Methods = Allow operations related to the class itself.
# take (cls) as the first parameter , which represents the class itself.

# Instance methods --> Best for operations on Instances of the class (objects).
#Static methods --> Best for utility functions that do not need access to class data
# Class methods --> Best for class-level data or require access to the class itself.

class Students :

    count = 0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Students.count+=1
        Students.total_gpa+=gpa

    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"total # of students :{cls.count}"
    @classmethod
    def get_average(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average gpa{cls.total_gpa/cls.count:.2f}"

stud1=Students("SpongeBob" , 3.2)
stud2=Students("Mayank",4.2)
stud3=Students("Himanshu",5.0)

print(Students.get_count())
print(Students.total_gpa())
