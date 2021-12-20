# Creating a Function
def my_function():
  print("Hello from a CQPOCS")

# Calling a Function
def my_function2():
      print("Hello from a CQPOCS2")

# calling function
my_function()
my_function2()

# Arguments
# Information can be passed into functions as arguments.
def my_function(fname):
      print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
      print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
def my_function(x):
      return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
def myfunction():
  pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# ***** The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power.*****
def tri_recursion(k):
      if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
      else:
        result = 0
      return result

print("\n\nRecursion Example Results")
tri_recursion(6)