# Variable scope = where a variable is visible and accessible.
# Scope Resolution = (LEGB) Local ->Enclosed->Global->Built-in

# Local Scope only function 1 has the acess of his x and function 2 have acess of its x they didnot have acess of  each other x.
def func1():
    x = 1 
    print(x)

def func2():
    x = 5
    print(x)

func1()
func2()


#  Enclosed scope is the scope of variables defined in an outer function that can be accessed by an inner (nested) function
def outer():
    x = 10

    def inner():
        x = 20
        print(x)

    inner()
    print(x)

outer()

# global --> if no local variables then functions can acess global values that is declared outside the functions.

x = 10
def func3():
    print(x)

def func4():
    x=5   # local variable will be prioritised ahead of global variables.
    print(x)

func3()
func4()


# built in --> preexisting whose values are built in.
import math
print(math.e) # e is the built in .

e = 10
print(e) #global is prioritized than built -in means if both exits python will print global variable.