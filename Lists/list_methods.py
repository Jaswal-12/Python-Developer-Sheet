# 📋 PYTHON LIST METHODS
# --------------------
# Lists are mutable, which means we can change, add,
# or remove elements after creation.

# ---------------------------------------
# Creating a List
# ---------------------------------------

l = [1, 2, 3, 5]
print("Original List:", l)

# ---------------------------------------
# append() -> Adds element at the end
# ---------------------------------------

l.append(6)
print("After append:", l)

# ---------------------------------------
# sort() -> Sorts the list in ascending order
# ---------------------------------------

l.sort()
print("After sort:", l)

# ---------------------------------------
# reverse() -> Reverses the list order
# ---------------------------------------

l.reverse()
print("After reverse:", l)

# ---------------------------------------
# index() -> Returns index of first occurrence
# ---------------------------------------

print("Index of 1:", l.index(1))

# ---------------------------------------
# count() -> Counts how many times an element appears
# ---------------------------------------

print("Count of 1:", l.count(1))

# ---------------------------------------
# Modifying an element using index
# ---------------------------------------

l[0] = 100
print("After modification:", l)

# ---------------------------------------
# insert() -> Inserts element at a specific index
# ---------------------------------------

l.insert(2, 200)
print("After insert:", l)

# ---------------------------------------
# extend() -> Adds elements of another list
# ---------------------------------------

m = [345, 345, 345]
l.extend(m)
print("After extend:", l)

# ---------------------------------------
# Additional Useful List Methods
# ---------------------------------------

# pop() -> Removes last element
l.pop()
print("After pop:", l)

# remove() -> Removes specific element
l.remove(345)
print("After remove:", l)

# ---------------------------------------
# List Length
# ---------------------------------------

print("Length of list:", len(l))

# ---------------------------------------
# Looping through a list
# ---------------------------------------

for item in l:
    print(item)

# ---------------------------------------
# Summary
# ---------------------------------------
# append()  -> add element at end
# sort()    -> sort list
# reverse() -> reverse list
# index()   -> find index of element
# count()   -> count element
# insert()  -> insert at position
# extend()  -> add another list
# pop()     -> remove last element
# remove()  -> remove specific element
