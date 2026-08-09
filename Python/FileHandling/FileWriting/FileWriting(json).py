# Json file writing

import json

employee={
    "name":"mayank",
    "age":30,
    "job":"Software Engineer"
}

file_path="Python\\FileHandling\\FileWriting\\output.json"

# with will defaulty close file at last
with open(file_path,"w") as file:
    # dump method will convert dictionary into a json string
    # indent will provide indent of 4.
    json.dump(employee,file,indent=4)
    print(f"txt file {file_path} was created")


