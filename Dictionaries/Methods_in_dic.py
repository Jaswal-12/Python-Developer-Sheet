"""
Python Dictionary Methods – Complete Guide with Examples
======================================================

This file explains the most commonly used dictionary methods in Python
with clear examples and professional explanations.

Author: Karan I
"""

# --------------------------------------------------
# 1. CREATING A DICTIONARY
# --------------------------------------------------

dic = {
    "name": "Karan",
    "course": "B.Tech",
    "year": 3
}

print("Initial Dictionary:", dic)


# --------------------------------------------------
# 2. get() METHOD
# --------------------------------------------------

"""
get() returns the value for a given key.
If the key does not exist, it returns None (or a default value).
"""

print("Name:", dic.get("name"))
print("Age (not present):", dic.get("age"))
print("Age with default:", dic.get("age", 21))


# --------------------------------------------------
# 3. keys() METHOD
# --------------------------------------------------

"""
keys() returns a view object containing all dictionary keys.
"""

print("Keys:", dic.keys())


# --------------------------------------------------
# 4. values() METHOD
# --------------------------------------------------

"""
values() returns a view object containing all dictionary values.
"""

print("Values:", dic.values())


# --------------------------------------------------
# 5. items() METHOD
# --------------------------------------------------

"""
items() returns key-value pairs as tuples.
Useful for looping through dictionaries.
"""

print("Items:", dic.items())

for key, value in dic.items():
    print(key, "->", value)


# --------------------------------------------------
# 6. update() METHOD
# --------------------------------------------------

"""
update() adds new key-value pairs or updates existing ones.
"""

dic.update({"year": 4, "university": "Chitkara University"})
print("After update:", dic)


# --------------------------------------------------
# 7. pop() METHOD
# --------------------------------------------------

"""
pop() removes a key-value pair and returns the value.
Raises KeyError if the key does not exist.
"""

removed = dic.pop("course")
print("Removed value:", removed)
print("After pop:", dic)


# --------------------------------------------------
# 8. popitem() METHOD
# --------------------------------------------------

"""
popitem() removes and returns the last inserted key-value pair.
"""

last_item = dic.popitem()
print("Popped item:", last_item)
print("After popitem:", dic)


# --------------------------------------------------
# 9. clear() METHOD
# --------------------------------------------------

"""
clear() removes all items from the dictionary.
"""

dic.clear()
print("After clear:", dic)


# --------------------------------------------------
# 10. copy() METHOD
# --------------------------------------------------

"""
copy() creates a shallow copy of the dictionary.
"""

original = {"a": 1, "b": 2}
copied = original.copy()

print("Original:", original)
print("Copied:", copied)


# --------------------------------------------------
# 11. setdefault() METHOD
# --------------------------------------------------

"""
setdefault() returns the value of a key.
If key does not exist, it inserts the key with a default value.
"""

student = {"name": "Karan"}
student.setdefault("age", 21)
print("After setdefault:", student)


# --------------------------------------------------
# 12. REAL-WORLD EXAMPLE
# --------------------------------------------------

"""
Dictionary methods are widely used in real-world applications
like managing user profiles and configuration data.
"""

user_profile = {
    "username": "karan12",
    "email": "karan@example.com",
    "active": True
}

# Update profile
user_profile.update({"active": False})

# Safe access
print("User Email:", user_profile.get("email"))


# --------------------------------------------------
# 13. SUMMARY
# --------------------------------------------------

"""
Key Takeaways:
- get() safely accesses values
- keys(), values(), items() are used for iteration
- update() modifies dictionary
- pop(), popitem() remove elements
- clear() empties dictionary
- copy() duplicates dictionary
- setdefault() inserts default values

These methods are very important for Python interviews
and real-world development.
"""
