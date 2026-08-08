# Decorator = a function that extends the behaviour of another function without modifying the base function
# Pass the base function as an argument to the decorator

def add_sprinkles(func):
    # without wrapper withou calling getice cream it will automatically run if you write @addsprinkles so wrapper is must
    def wrapper(*args,**kwargs):
        print("You added sprinkles")
        func(*args,**kwargs)

    return wrapper

def add_fudges(func):
    def wrapper(*args,**kwargs):
        print("You added fudges")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles #get_ice_cream = add_sprinkles(get_ice_cream)
@add_fudges # it will run first because below one gets the priority
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")


get_ice_cream("vanilla")