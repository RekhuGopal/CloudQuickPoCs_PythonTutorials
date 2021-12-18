## python list - ordered
mylist = ["A", "C", "C"]

print(mylist)

## allow duplicates and changeable
thislist = ["A", "B", "C", "A", "C"]
print(thislist)
thislist.append("O")
print(thislist)


## list length.
thislist = ["A", "B", "C"]
print(len(thislist))


## the list() constructor
thislist = list(("A", "B", "C"))
print(thislist)

######################################### Accessing the list ####################################################
thislist = ["A", "B", "C"] # thislist[0]/thislist[-3] =  A , thislist[1]/thislist[-2] =  B , thislist[2]/thislist[-1] =  c
## positive indexing
print(thislist[1])
## negetive indexing   # length = 3 , negative index = (positive index - length of list)
print(thislist[-1])
## Range of Indexes
print(thislist[0:2])
## Starting from first to a range
print(thislist[:4])
## From end to a range
print(thislist[2:])
## negative range
print(thislist[-4:-1])
## Check if item exists
if "A" in thislist:
      print("Yes, 'A' is in the fruits list")

######################################### Change list items ####################################################
thislist = ["A", "B", "C"]
thislist[1] = "b"
print(thislist)
thislist.insert(2, "w")
print(thislist)
## Range replacements
thislist[1:3] = ["b", "w"]
print(thislist)

######################################### Add list items ####################################################
# append() To add an item to the end of the list
thislist = ["A", "B", "C"]
thislist.append("O")
print(thislist)

# insert() To insert a list item at a specified index
thislist.insert(1, "O")
print(thislist)

# extend() To append elements from another list to the current list
thislist = ["A", "B", "C"]
tropical = ["m", "pi", "p"]
thislist.extend(tropical)
print(thislist)

######################################### Remove list items ####################################################
# The remove() method removes the specified item.
thislist = ["A", "B", "C"]
thislist.remove("B")
print(thislist)

# The pop() method removes the specified index (do not specify the index, the pop() method removes the last item).
thislist = ["A", "B", "C"]
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)

# The del keyword also removes the specified index (The del keyword can also delete the list completely.):
thislist = ["A", "B", "C"]
del thislist[0]
print(thislist)

# The clear() method empties the list.
thislist = ["A", "B", "C"]
thislist.clear()
print(thislist)

######################################### Loop list items ######################################################################
# Loop Through a List
thislist = ["A", "B", "C"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
thislist = ["A", "B", "C"]
for i in range(len(thislist)): # 0 , 1, 2
  print(thislist[i])

# Using a While Loop
thislist = ["A", "B", "C"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["A", "B", "C"]
[print(x) for x in thislist]


######################################### List Comprehension ####################################################
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

## Without comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

## with comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

######################################### List Sort ##################################################################
# List objects have a sort() method that will sort the list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort numebr list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort the list descending (after sorting make reverse)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# reverse the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

######################################### Copy Lists ##################################################################
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


######################################### Join Lists ##################################################################
# join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# appending (append()) each element
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#  Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)