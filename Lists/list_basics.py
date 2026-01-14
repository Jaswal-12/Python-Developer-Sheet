# 📋 PYTHON LISTS
# --------------
# A list is a collection of items stored in a single variable.
# Lists are:
# ✔ Ordered
# ✔ Mutable (can be changed)
# ✔ Can store multiple data types
# ✔ Written using square brackets []

# ---------------------------------------
# Creating a List
# ---------------------------------------

l = [1, 2, 3, 4]
print(l)
print(type(l))

# ---------------------------------------
# Accessing Elements (Indexing)
# ---------------------------------------
# Index starts from 0

print(l[0])   # 1
print(l[1])   # 2
print(l[2])   # 3

# ---------------------------------------
# Lists Can Store Multiple Data Types
# ---------------------------------------

l1 = [3, 5, 6, "jass", True, 4.5]
print(l1)

# ---------------------------------------
# Modifying a List (Mutability)
# ---------------------------------------

l[1] = 20     # Changing element at index 1
print(l)

# ---------------------------------------
# List Length
# ---------------------------------------

print("Length of list:", len(l))

# ---------------------------------------
# Adding Elements to a List
# ---------------------------------------

l.append(50)      # Adds element at the end
print(l)

l.insert(1, 100)  # Inserts at specific index
print(l)

# ---------------------------------------
# Removing Elements from a List
# ---------------------------------------

l.remove(100)     # Removes specific element
print(l)

l.pop()           # Removes last element
print(l)

# ---------------------------------------
# Looping Through a List
# ---------------------------------------

for item in l1:
    print(item)

# ---------------------------------------
# List Slicing
# ---------------------------------------

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# ---------------------------------------
# Checking if Element Exists
# ---------------------------------------

print(20 in numbers)   # True
print(100 in numbers)  # False

# ---------------------------------------
# Summary
# ---------------------------------------
# - Lists are ordered and mutable
# - Indexing starts from 0
# - Lists can store different data types
# - Useful methods: append(), insert(), remove(), pop()
