# If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# If , Elif , Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
a = 33
b = 200
if b > a:
  pass