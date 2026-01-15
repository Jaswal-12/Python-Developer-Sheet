"""
Python Tuples
--------------

A tuple is a built-in data type in Python used to store multiple items
in a single variable.

Key Characteristics of Tuples:
1. Ordered
2. Immutable (cannot be changed after creation)
3. Allows duplicate values
4. Can store multiple data types
5. Faster than lists (in some cases)
"""

# -------------------------------
# Creating a Tuple
# -------------------------------
tp = (1, 3, 45, 53, 3, 2, 4)
print("Tuple:", tp)

# -------------------------------
# Type of Tuple
# -------------------------------
print("Type:", type(tp))

# -------------------------------
# Accessing Tuple Elements
# -------------------------------
print("First element:", tp[0])
print("Last element:", tp[-1])

# -------------------------------
# Tuple with Different Data Types
# -------------------------------
mixed_tuple = (1, "Karan", 3.5, True)
print("Mixed Tuple:", mixed_tuple)

# -------------------------------
# Tuple with Single Element
# (Comma is mandatory)
# -------------------------------
single_element_tuple = (5,)
print("Single Element Tuple:", single_element_tuple)

# -------------------------------
# Tuple Slicing
# -------------------------------
print("Sliced Tuple (index 1 to 4):", tp[1:5])

# -------------------------------
# Iterating Over a Tuple
# -------------------------------
print("Iterating over tuple:")
for item in tp:
    print(item)

# -------------------------------
# Tuple Methods
# -------------------------------
print("Count of 3:", tp.count(3))
print("Index of 45:", tp.index(45))

# -------------------------------
# Tuple Immutability
# (This will cause an error if uncommented)
# -------------------------------
# tp[0] = 100   # ❌ Not allowed

# -------------------------------
# Converting Tuple to List
# -------------------------------
temp_list = list(tp)
temp_list.append(99)
tp = tuple(temp_list)
print("Tuple after conversion:", tp)

# -------------------------------
# Tuple Packing and Unpacking
# -------------------------------
student = ("Karan", 21, "Python Developer")
name, age, role = student
print("Name:", name)
print("Age:", age)
print("Role:", role)

"""
When to Use Tuples?
------------------
- When data should not be changed
- For fixed collections (coordinates, days, config values)
- For better performance and safety
"""
