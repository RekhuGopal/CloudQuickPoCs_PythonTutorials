## Varaibels decalration
x = 5
y = "Lion"
print(x)
print(y)

## Variables overwritting
x = 4       # x is of type int
x = "Sunday" # x is now of type str
print(x)

## Case senstives
A =  "AWS"
a =  "Azure"
print(a)
print(A)

## Variabels casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


## Check data types
print(type(x))


## Assign values to multiple variables in one line:
x, y, z = "A", "B", "C"
print(x)
print(y)
print(z)

## Assign the same value to multiple variables in one line:
x = y = z = "CQPOCs"
print(x)
print(y)
print(z)

## Unpack a Collection
fruits = ["X1", "X2", "X3"]
x, y, z = fruits
print(x)
print(y)
print(z)

## Output variables
x = "youtube"
print("Python learning on " + x)

## Global varibles (created outside function).
x = "youtube"

def myfunc():
  print("Python learning on " + x)

myfunc()

## Global varibles (created inside function with using 'global' key).
def myfunc2():
    global x
    x = "fantastic"
myfunc2()

print("Python is " + x)
