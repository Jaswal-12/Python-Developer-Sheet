# 🧵 STRING METHODS IN PYTHON
# -------------------------
# Strings in Python are IMMUTABLE.
# This means string methods return a NEW string
# and do NOT change the original string.

a = "karan"

# ---------------------------------------
# Case Conversion Methods
# ---------------------------------------

print(a.upper())    # KARAN  -> converts to uppercase
print(a.lower())    # karan  -> converts to lowercase
print(len(a))       # 5      -> length of the string

# ---------------------------------------
# Removing Unwanted Characters
# ---------------------------------------

b = "adjdijaidj!!!!!##"

print(b.rstrip("!"))   # removes ! from the right side
print(b.rstrip("#"))   # removes # from the right side

# ---------------------------------------
# Replacing Characters
# ---------------------------------------

print(a.replace("karan", "jaswal"))  # replaces karan with jaswal

# ---------------------------------------
# Splitting a String
# ---------------------------------------

sentence = "Hello Python Developer"
print(sentence.split(" "))   # splits into a list of words

# ---------------------------------------
# Capitalize & Count
# ---------------------------------------

x = "intro to python developer"

print(x.capitalize())  # Intro to python developer
print(x.count('e'))    # counts how many times 'e' appears

# ---------------------------------------
# Checking Start and End
# ---------------------------------------

print(x.endswith('er'))   # True
print(x.startswith('in')) # True

# ---------------------------------------
# Finding a Substring
# ---------------------------------------

print(x.find('to'))  # gives index of 'to'

# ---------------------------------------
# Checking String Content
# ---------------------------------------

print(x.isalnum())   # False (contains spaces)
print(a.isalpha())  # True (only letters)
print(a.islower())  # True (all lowercase)

# ---------------------------------------
# Strings are Immutable
# ---------------------------------------
# a[0] = "R"   ❌ This is not allowed
# Instead:
new_a = "R" + a[1:]
print(new_a)
