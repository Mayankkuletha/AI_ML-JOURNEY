# Python writing files(.txt,.json,.csv)

txt_data=" I Like pizza"
employees =["Euguene" , "Squidward" , "SpongBob", "Patrick"]


file_path = "Python\\FileHandling\\output.txt"

# w--->In this way we can write in a file and if it does not exit it will automatically create it and if we add new data it will overwrite old data.
# try: 
#     with open(file_path,"w") as file:
#         file.write(txt_data)
#         print(f"File '{file_path}'created succesfully")
# except FileExistsError:
#     print("File already exits")

# x--> this is also same as w but in x if file already exits it will show error.

# try: 
#     with open(file_path,"x") as file:
#         file.write(txt_data)
#         print(f"File '{file_path}'created succesfully")
# except FileExistsError:
#     print("File already exits")

# a -->append --> we can append data in the file it will also create file if not exist. and continue adding data ahead of old data
try: 
    with open(file_path,"a") as file:
        # file.write(txt_data)
        # file.write("\n"+txt_data)
        # file.write(employees) # we can acess list directly we have to pass str
        for emp in employees:
         file.write(emp + "\n")

        print(f"File '{file_path}'created succesfully")
except FileExistsError:
    print("File already exits")

