# Python Reading file (.txt)

file_path = "Python\\FileHandling\\FileWriting\\output.txt"

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



