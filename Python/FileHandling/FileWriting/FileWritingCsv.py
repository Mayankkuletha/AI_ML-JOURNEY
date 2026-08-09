# Csv file writing
import csv

employee = [["Name" , "age" , "Job"],
            ["Mayank",20,"null"],
            ["Himanshu",22,"null"],
            ["Karan",21,"null"],
            ]

file_path ="Python\\FileHandling\\FileWriting\\output.csv"

with open(file_path,"w",newline="") as file:
    writer = csv.writer(file) #Yahan csv.writer() ek writer object banata hai.
    for row in employee:
        # writer gives automatic space so we have newline = "" to remove that extra space
        writer.writerow(row)

    print(f"{file_path} was sucessfully Created")