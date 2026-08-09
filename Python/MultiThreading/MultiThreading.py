# MultiThreading--> Used to perform multiple task concurrently (multitasking).
# Good for I/O bound tasks like reading files or fetching data from Apis
# Threading.Thread(target_my_function)

import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# IN this way without multithreading program will execute sequentially others programs with less time are unnecassrily waiting . So we use the concept of multithreading.
# walk_dog("Scooby","dog")
# take_out_trash()
# get_mail()

chore1=threading.Thread(target=walk_dog , args=("Scobby" , "Doo")) #single argument k bd comma lgana wrna error 
# Because Python me:
# ("Mayank")
# sirf ek string hai.
# Lekin:
# ("Mayank",)
# tuple containing one item hai.
chore1.start()
chore2=threading.Thread(target=take_out_trash)
chore2.start()
chore3=threading.Thread(target=get_mail)
chore3.start()
chore1.join()
chore2.join()
chore3.join()

print("All chores completed") #Join k bina y phle he execute ho jata join khta ki khtm hone ka intzar kro .