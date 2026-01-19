"""
enumerate_function_demo.py

This file demonstrates the use of Python's enumerate() function
with multiple examples and explanations.

🔹 What is enumerate()?

enumerate() is a built-in Python function that allows you to loop
over a sequence (such as a list, tuple, or string) while keeping
track of both:
1. The index (position)
2. The value (element)

It is commonly used as a cleaner and more readable alternative
to using range(len()).

Syntax:
    enumerate(iterable, start=0)

Parameters:
- iterable : Any iterable object (list, string, tuple, etc.)
- start    : (Optional) Starting index value (default is 0)
"""

# -------------------------------
# Example 1: Basic enumerate usage
# -------------------------------

marks = [12, 45, 14, 67, 84, 23, 45, 12, 34, 56, 78, 9]

print("Example 1: Enumerating marks list\n")

for index, mark in enumerate(marks):
    print("Mark:", mark, "Index:", index)

    # Condition using index
    if index == 5:
        print("Karan Awesome")

print("\n" + "-" * 40 + "\n")

# -------------------------------------
# Example 2: enumerate with start index
# -------------------------------------

print("Example 2: enumerate with start=1\n")

# Here indexing starts from 1 instead of 0
for index, mark in enumerate(marks, start=1):
    print("Student No:", index, "Marks:", mark)

print("\n" + "-" * 40 + "\n")

# -------------------------------------
# Example 3: enumerate with strings
# -------------------------------------

name = "KARAN"

print("Example 3: enumerate with a string\n")

# Strings are iterable, so enumerate works on them
for index, letter in enumerate(name):
    print("Index:", index, "Letter:", letter)

print("\n" + "-" * 40 + "\n")

# -------------------------------------
# Example 4: enumerate with condition
# -------------------------------------

print("Example 4: Find marks greater than 60\n")

for index, mark in enumerate(marks):
    if mark > 60:
        print(f"Index {index} has high marks: {mark}")

print("\n" + "-" * 40 + "\n")

# -------------------------------------
# Example 5: enumerate vs range(len())
# -------------------------------------

print("Example 5: enumerate vs range(len())\n")

print("Using range(len()):")
for i in range(len(marks)):
    print("Index:", i, "Mark:", marks[i])

print("\nUsing enumerate():")
for i, mark in enumerate(marks):
    print("Index:", i, "Mark:", mark)

"""
Why enumerate() is better than range(len())?

✔ Cleaner and more readable
✔ No need to manually access elements using index
✔ Less error-prone
✔ Preferred in professional and interview-level code
"""
