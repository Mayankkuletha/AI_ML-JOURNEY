# Exception - An event that interrupts the flow of a program
# ZeroDivisionError,TypeError,ValueError
# 1.Try 2.Except 3.Finally

try:
  number = int(input("Enter a number"))
  print(1/number)
except ZeroDivisionError :
  print("You cant divide by Zero Idiot")
except ValueError :
  print("Enter only numbers Please")
except Exception:
  print("Something Went Wrong")
finally:
  print("Do some cleanup Here")

 