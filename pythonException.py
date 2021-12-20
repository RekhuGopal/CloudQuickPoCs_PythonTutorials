## Example try/except statement usage (catch KeyErrors in a dictionary)
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

## cathing different types of exceptions
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other problem happened!")

## try/except with else clause
my_dict = {"a":1, "b":2, "c":3}
try:
    b= 8/0
except ZeroDivisionError:
    print("A Zero Division Error occurred!")
else:
    print("No error occurred!")

## General catching all exceptions
try:
    a =  7/0
except Exception as exception:
    print("Error occured and error is", exception)