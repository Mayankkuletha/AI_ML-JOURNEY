# module --> a file containing code you want to include in your program
# use import to include a module(built-in or your own)
#useful to break up a large program reusable seprate files

# import math
# print(math.pi)

# import math as m 
# print(m.pi)

print(help("modules")) #it will give you the list of all modules
from math import e
print(e)
# above method is not prefered always because what if 
a,b,c,d,e=1,2,3,4,5
print(e*e)
# so it will take variable value instead of imported one.