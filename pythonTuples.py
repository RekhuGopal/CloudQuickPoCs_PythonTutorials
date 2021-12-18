# Create tuples
thistuple = ("A", "B", "C")
print(len(thistuple))

# One item tuple, remember the comma:
thistuple = ("A",)
print(type(thistuple))

#NOT a tuple
thistuple = ("A")
print(type(thistuple))

################################## Access Tuple Items #######################################
# positive indexing
thistuple = ("A", "B", "C")  # thistuple[0] =  A , thistuple[1] =  B, thistuple[2] =  C , length = 3
print(thistuple[1])

# negative indexing
thistuple = ("A", "B", "C" )  # negetive index =  (positive index - length tuble) , cth negetive index =  2-3 = -1
print(thistuple[-1])

# range of indexing
thistuple = ("A", "B", "C", "O", "k", "M", "m")
print(thistuple[2:5])

# check if item exists
thistuple = ("A", "B", "C")
if "A" in thistuple:
  print("Yes, 'A' is in the fruits tuple")

################################## Update Tuple Items #######################################
# Change Tuple Values
x = ("A", "B", "C")
print(type(x))
y = list(x)
print(type(y))
y[1] = "k"
x = tuple(y)

print(x)

# Add Items - convert the tuple into a list, add "O", and convert it back into a tuple:
thistuple = ("A", "B", "C")
y = list(thistuple)
y.append("O")
thistuple = tuple(y)

# Add Items - Create a new tuple with the value "O", and add that tuple:
thistuple = ("A", "B", "C")
y = ("O",)
thistuple += y
print(thistuple)

# Remove Items
thistuple = ("A", "B", "C")
y = list(thistuple)
y.remove("A")
thistuple = tuple(y)

################################## Unpack Tuple Items #######################################
# Unpacking a tuple:
fruits = ("A", "B", "C")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk* : Assign the rest of the values as a list called "red"
fruits = ("A", "B", "C", "s", "r")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

################################## Loop Through a Tuple #######################################

# for loop
thistuple = ("A", "B", "C")
for x in thistuple:
  print(x)

# for loop with range() and len()
thistuple = ("A", "B", "C")
for i in range(len(thistuple)):
  print(thistuple[i])

# whie loop
thistuple = ("A", "B", "C")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


################################## Join a Tuple ##################################################
# join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2:
fruits = ("A", "B", "C")
mytuple = fruits * 2

print(mytuple)