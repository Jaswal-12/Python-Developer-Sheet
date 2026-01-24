"""
LAMBDA FUNCTIONS IN PYTHON
-------------------------
This file explains lambda (anonymous) functions with
clear examples and use-cases.

Author: Karan
"""

# ==========================================================
# 1. What is a lambda function?
# ==========================================================
# A lambda function is a small, anonymous function.
# It can take ANY number of arguments but has ONLY ONE expression.
#
# Syntax:
# lambda arguments : expression

# ==========================================================
# 2. Basic lambda examples
# ==========================================================

# Square of a number
square = lambda x: x * x
print("Square of 5:", square(5))

# Cube of a number
cube = lambda x: x * x * x
print("Cube of 5:", cube(5))

# Average of two numbers
avg = lambda x, y: (x + y) / 2
print("Average of 5 and 3:", avg(5, 3))

# ==========================================================
# 3. Lambda vs Normal function
# ==========================================================

# Normal function
def add(a, b):
    return a + b

# Lambda function
add_lambda = lambda a, b: a + b

print("Normal function add:", add(4, 6))
print("Lambda function add:", add_lambda(4, 6))

# ==========================================================
# 4. Lambda with conditional expression
# ==========================================================
# Syntax:
# lambda x : value_if_true if condition else value_if_false

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("10 is:", is_even(10))
print("7 is:", is_even(7))

# ==========================================================
# 5. Lambda with multiple arguments
# ==========================================================

max_of_two = lambda a, b: a if a > b else b
print("Max of 10 and 20:", max_of_two(10, 20))

# ==========================================================
# 6. Lambda with built-in functions
# ==========================================================

numbers = [1, 2, 3, 4, 5]

# map() -> applies function to each element
squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)

# filter() -> filters elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# reduce() -> reduces list to a single value
from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce():", sum_all)

# ==========================================================
# 7. Lambda for sorting
# ==========================================================

students = [
    ("Karan", 90),
    ("Aman", 85),
    ("Rohit", 92)
]

# Sort by marks
students_sorted = sorted(students, key=lambda x: x[1])
print("Students sorted by marks:", students_sorted)

# ==========================================================
# 8. Limitations of lambda functions
# ==========================================================
# - Only ONE expression allowed
# - No statements (loops, assignments)
# - Less readable for complex logic
# - Best for SHORT and SIMPLE operations

# ==========================================================
# 9. When to use lambda?
# ==========================================================
# ✔ Short functions
# ✔ One-time use
# ✔ With map(), filter(), sorted()
# ❌ Avoid for complex logic

print("\nLambda function examples executed successfully.")

