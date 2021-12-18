# Print each fruit in a fruit list:
fruits = ["A", "B", "C"]
for x in fruits:
  print(x)

# Looping Through a String
for x in "PYTHON":
  print(x)

# The break Statement
fruits = ["A", "B", "C"]
for x in fruits:
  print(x)
  if x == "B":
    break

# The continue Statement
fruits = ["A", "B", "C"]
for x in fruits:
  if x == "B":
    continue
  print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6): #range(6) = 0 ,1 ,2,3,4,5
  print(x)

# Using the start parameter:
# range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6): #range(2,6) = 2,3,4,5
  print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3): #range(2,30, 3) = 2,5,8,11...29
  print(x)

# Else in For Loop
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
      print(x)
else:
      print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6): #range(6) = 0 ,1 ,2,3,4,5
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Nested for Loops
adj = ["red", "big", "tasty"]
fruits = ["A", "B", "C"]
for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
for x in [0, 1, 2]:
  pass