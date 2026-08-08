# Magic Methods = Dunder methods (double underScore) __init__ , __str__,__eq__
# They are automatically called by many of Pythons built in opeartions.
# They allow developers to define or customize the behaviour of objects.

# Inhe "magic" isliye bolte hain kyunki Python in methods ko automatically call kar sakta hai jab hum kuch normal operation karte hain.
class Book :
    #__init__ is an constructor here.
    #simply gives object which is not useful so we use __str__ 
    def __init__(self , title , author , num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} , ({self.author})"

    # for checking two objects are equal or not.
    def __eq__(self, other):
        return self.title==other.title and self.author==other.author

    # for less than
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # for greater than
    def __gt__(self, other):
        return self.num_pages>other.num_pages

    # for adding two objects
    def __add__(self, other):
        return self.num_pages + other.num_pages

    # for calculating length of object things
    def __len__(self):
        return len(self.author)

    # anything exits in object or not.
    def __contains__(self, item):
        return item in self.title

    # to get any item
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == self.num_pages:
            return self.num_pages
        else :
            return f"key {key} was not found"
book1 = Book("Harry Potter", "J.K. Rowling", 500)
book2= Book("The Hobbit", "J.R.R. Tolkien", 300)

# print(book1) 
print(book1==book2)

print(book1<book2)
print(book1>book2)
print(book1+book2)
print(len(book1))
print("Harry" in book1)

print(book1["author"])


