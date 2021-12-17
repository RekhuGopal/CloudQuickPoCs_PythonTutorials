## single arguement formating in string
age = 26
txt = "My name is bob, and I am {}"
print(type(txt))
print(txt.format(age))

## multiple arguement formating in string
quantity = 4
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))