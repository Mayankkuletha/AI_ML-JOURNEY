# Json file reading

import json

file_path= "Python\\FileHandling\\FileWriting\\output.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)
        # json.load() ka kaam JSON file ko read karke Python object me convert karna hota hai.
        # print(content)
        print(content["name"]) #we can acess value like this also.
except FileNotFoundError:
     print("That file was not found")
    
