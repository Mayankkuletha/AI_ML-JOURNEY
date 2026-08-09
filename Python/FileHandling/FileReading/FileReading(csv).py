# Reading Csv file

import csv 

file_path="Python\\FileHandling\\FileWriting\\output.csv"

with open(file_path,"r") as file:
    content = csv.reader(file) 
    # print(content) #it will return object 
    # In csv we have a collection of things so we will aplly loop 

    for line in content:
        # print(line)
        print(line[0]) #In this we can acesss single things.