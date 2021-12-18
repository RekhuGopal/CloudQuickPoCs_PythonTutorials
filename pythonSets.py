# Create a Set:
thisset = {"A", "B", "C"}
print(thisset)

# Duplicate values will be ignored:
thisset = {"A", "B", "C", "A"}
print(thisset)

# Get the number of items in a set:
thisset = {"A", "B", "C"}
print(len(thisset))

######################################## Access Sets Items ################################################################################

# You cannot access items in a set by referring to an index or a key.
thisset = {"A", "B", "C"}
for x in thisset:
  print(x)


# Check if "B" is present in the set:
thisset = {"A", "B", "C"}
print("B" in thisset)

######################################## Add Sets Items ##################################################################################
# Add an item to a set, using the add() method:
thisset = {"A", "B", "C"}
thisset.add("O")
print(thisset)


# Add elements from tropical into thisset:
thisset = {"A", "B", "C"}
tropical = {"A", "M", "P"}
thisset.update(tropical)
print(thisset)

# Add elements of a list to at set:
thisset = {"A", "B", "C"}
mylist = ["K", "O"]
thisset.update(mylist)
print(thisset)


######################################## Remove Sets Items ##################################################################################

# Remove "B" by using the remove() method:
thisset = {"A", "B", "C"}
thisset.remove("B")
print(thisset)

# Remove "B" by using the discard() method:
thisset = {"A", "B", "C"}
thisset.discard("B")
print(thisset)

# Remove the last item by using the pop() method:
thisset = {"A", "B", "C"}
x = thisset.pop()
print(x)
print(thisset)


# The clear() method empties the set:
thisset = {"A", "B", "C"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"A", "B", "C"}
del thisset
#print(thisset)

######################################## Loops Sets Items ##################################################################################

# Loop through the set, and print the values:
thisset = {"A", "B", "C"}
for x in thisset:
  print(x)


######################################## Join Sets Items ##################################################################################

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Keep the items that exist in both set x, and set y:
x = {"A", "B", "C"}
y = {"google", "microsoft", "A"}
x.intersection_update(y)
print(x)

# Return a set that contains the items that exist in both set x, and set y:
x = {"A", "B", "C"}
y = {"google", "microsoft", "A"}
z = x.intersection(y)
print(z)

# Keep the items that are not present in both sets:
x = {"A", "B", "C"}
y = {"google", "microsoft", "A"}
x.symmetric_difference_update(y)
print(x)

# Return a set that contains all items from both sets, except items that are present in both:
x = {"A", "B", "C"}
y = {"google", "microsoft", "A"}
z = x.symmetric_difference(y)
print(z)