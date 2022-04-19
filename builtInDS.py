
# LISTS
#Mutable Built-in DS

print("LISTS")
a = [23, 56, "Klaus", 29.4]
print("List A: ", a)

b = []
print("List B: ", b)

# Appending a list
b.append(45)
b.append(34)
b.append(76)
print("Appended List B: ", b)
b.insert(2, 99) # We van also insert a list into a list


# Removing List Item
a.remove(56)
print("Removed 56 List A: ", a)

# Replacing List Item
# Only works if lists have same data type (array list)
# This cannot work with List a
b[3] = 50
print("Replaced third element List B: ", b, "\n")

# Index and Item in a list

for item in b:
    print(item)

print("index item")
for index, item in enumerate(b):
    print(index, "   ", item)
print("\n")

# Number of items in a list
print("Number of elements in list A is: ", len(a))
print("Number of elements in list B is: ", len(b), "\n")

# Sort list
print("Sorted List B: ", sorted(b), "\n")

# We can also find min(b), max(b), etc


# Testing element existence in list
print("56 is not in A: ", 56 in a)
print("Klaus is in A: ", "Klaus" in a)
print("50 is not in B: ", 50 in b)
print("34 in not in B: ", 34 not in b, "\n")

# List concatenation and multiplication
print("Concatenates Lists A and B: ", a + b, "\n")
print("prints List A trice: ", a*3, "\n")

# Popping off items at the end of the list
print(b.pop(), " Has been popped off from the list B and B becomes", b, "\n")

# Reverse order of list
b.reverse()
print("The order of B Has been reversed to: ", b, "\n")

# Sort
b.sort()
print("Sorted B: ", b)
b.sort(reverse=True)
print("Reverse Sort B: ", b, "\n")


# String Slicing
x = 'computer'
print("Below are slices from: ", x)
print(x[1:4]) # removes elements at index < 1 and index >= 4
print(x[1:6:2]) # prints elements at index >= 1 and index < 6 in steps of 2
print(x[3:]) # prints elements at index >= 3
print(x[:5]) # prints elements at index < 5
print(x[-1]) # Prints last element
print(x[-3:]) # Prints last three elements
print(x[:-2]) # Remove last two elements
print("\n\n")

# TUPLES
# Immutable Built-In DS (Concatenation can work, deletion from tuple element which is list)

print("TUPLES")
c = (3.3, -4.0, 5.2)
print("Tuple (x, y, z): ", c, "\n")

y = ([1, 9], 7)
print("Tuple Y: ", y)
del(y[0][1])  # Delete 9
print("Removed 9: ", y, )
y += (10, ) # Concatenating tuple
y += ([56, 78, [32, -43, [66, 11, 29]]], ) # Concatenating tuple
print("Concatenated Tuple Y: ", y)
del(y[3][2][1])  # Deletes -43
print("Removed -43: ", y)
del(y[3][2][1][1])  # Deletes 11
print("Removed 11: ", y, "\n\n")


# DICTIONARIES
# Used to store key-value pairs

print("DICTIONARIES")
d = {1: "Python", 2: "Javascript", 3: "Solidity", 4: "ReactJS", 5: "HTML-CSS", 6: "Java", 7: "C/C++"}
print("Dictionary: ", d,)

# Dictionary Operations
d[8] = "AngularJS"   # append
d[5] = "ReactJS"   # Update
d[4] = "HTML/CSS"
print("Updated Dictionary: ", d,)
del(d[8])
print("Deleted Item 8: ", d, "\n")

# Accessing Keys and Values in dictionary
print("All Keys: ", d.keys())
print("All values: ", d.values())
print("All key-value pairs: ", d.items(), "\n")

# Checking items in dictionary
print("Is Key 5 in Dictionary: ", 5 in d)
print("Is Python a Value: ", "Python" in d.values(), "\n")

# Iterating Dictionary

print("Iteration of Key-Value Pairs")
for key in d:
    print(key, d[key])

print("\n\n")

# Clear dictionary
d.clear()
# Delete dictionary and clear memory
del(d)

# SETS
# Collection of unordered elements that are unique (non-duplicate)
# Cannot Sort a set
# Great at searching element
print("SETS")
e = {5, 6, 22, 5, 7, 5, 22, 4, 8, 7}
f = {6, 2, 9, 0, 11, 7, 1, 3, 9}
g = {21, 22, 9, 41, 6, 41, 8, 3}

print("Set E: ", e)
print("Set F: ", f)
print("Set G:", g, "\n")

# Add and delete Elements in set
e.add(15)
print("Add 15 to E :", e)
f.remove(9)
print("Removes 9 from F: ", f, "\n")

# Pop a random item from set
print("The randomly popped item for G is: ", g.pop(), "\n")



# Set Operations
print("E U F: ", e.union(f))
print("E U G: ", e.union(g))
print("F U G: ", f.union(g))
print("E U F U G: ", e.union(f).union(g))
print("E n F: ", e.intersection(f))
print("E n G: ", e.intersection(g))
print("F n G: ", f.intersection(g))
print("E n F n G: ", e.intersection(f).intersection(g))
print("E-F: ", e-f,)
print("E-F-G: ", e-f-g, "\n")

print("ALTERNATIVE WAYS OF SET OPERATIONS")
print("E U G: ", e | g)
print("E n F: ", e & f)
print("F U G: ", f | g)
print("F ^ G: ", f ^ g) # elements found in f and elements found in g but not both (6 is found in both, so it is excluded)
print("E n F n G: ", e & f & g)
print("E is subset of F", e<=f)  # False
print("F is superset of G: ", f>=g, "\n") # False

# Deletes all elements from set
e.clear()
f.clear()
g.clear()
print("All elements deleted")
print("Set E: ", e)
print("Set F: ", f)
print("Set G:", g, "\n")

# Delete the sets
del(e)
del(f)
del(g)