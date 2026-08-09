# Python file detection
# os Python ka built-in module hai jo operating system ke saath kaam karne ke liye use hota hai.

# Jaise:

# file exist karti hai ya nahi
# file hai ya folder
# folder banana
# file delete karna etc.
import os

# Path can be of two types ---->  
# Relative --> folder/test.txt
# Absolute --> C:/Users/BroCode/Desktop/test.txt
file_path = "Python\\FileHandling\\file.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("Thats a file")
    elif os.path.isdir(file_path):
        print("Thats a directory")

else :
    print("That location doesnt exist")