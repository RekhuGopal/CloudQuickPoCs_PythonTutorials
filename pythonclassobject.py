# Create a class named ExampleClass, with a property named x:
class ExampleClass():
  x = 5

# Create an object named p1, and print the value of x:
p1 = ExampleClass()
print(p1.x)

# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Man("John", 36)
print(p1.name)
print(p1.age)

# Object Methods
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is {} and my age is {} ".format(self.name, self.age ))

p1 = Man("John", 36)
p1.myfunc()

# The self Parameter
class Man():
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is {} and my age is {} ".format(abc.name, abc.age ))

p1 = Man("John", 36)
p1.myfunc()

# Modify Object Properties
p1.age = 40
p1.myfunc()
# Delete Object Properties
del p1.age

# Delete Objects
del p1

# The pass Statement
class Man:
    pass