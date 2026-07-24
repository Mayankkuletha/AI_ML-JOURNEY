def calculator ():
    x=5+8
    print(x)

# print("Hello world")


# we just wanted to export function but hello world get unneccesirily printed so
# to avoid this we put if_name_="_main_" means only main user can acess this 
if __name__ == "__main__":
    print("Welcome")
    calculator()

