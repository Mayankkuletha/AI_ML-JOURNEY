# Class variable --> shared among all instance of a class
# Defined outside the constructor
# Allow you to share data among all objects created from that class

class Student :
    class_year = 2026
    num_students=0
    # self is the object we are currently working with
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 
        Student.num_students+=1

Student1=Student("SpongBob",30) #instance variables
Student2=Student("Pattrick",35)
Student3=Student("Mayank",20)

# print(Student2.name)
# print(Student2.age)
# print(Student.class_year) #its better to acess class Variable with Class name

print(f"The class year {Student.class_year} has {Student.num_students} students")
print(Student1.name)
print(Student2.name)
print(Student3.name)

        