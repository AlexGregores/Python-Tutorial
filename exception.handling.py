# exception = events detected during execution that interrupt the flow os a program 
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero idiot")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("something went wrong")
else:
    print(result)
#finally:
#    print("This is always execute")

