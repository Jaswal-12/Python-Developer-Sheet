"""
Python f-Strings (Formatted String Literals)
--------------------------------------------

f-strings were introduced in Python 3.6.
They provide a simple, readable, and efficient way
to format strings using variables and expressions.
"""

# ---------------------------------
# Example 1: Using format() method
# ---------------------------------
template = "My name is {} and my surname is {}"
name = "Karan"
surname = "Jaswal"

print(template.format(name, surname))

# ---------------------------------
# Example 2: Using f-strings (Recommended)
# ---------------------------------
print(f"My name is {name} and my surname is {surname}")

# ---------------------------------
# Example 3: Expressions inside f-strings
# ---------------------------------
a = 10
b = 20
print(f"Sum of a and b is {a + b}")
print(f"Product of a and b is {a * b}")

# ---------------------------------
# Example 4: Calling functions in f-strings
# ---------------------------------
def greet(user):
    return f"Hello, {user}!"

print(f"Greeting message: {greet(name)}")

# ---------------------------------
# Example 5: Formatting numbers
# ---------------------------------
price = 49.56789
print(f"Price rounded to 2 decimals: {price:.2f}")

# ---------------------------------
# Example 6: Using f-strings with lists
# ---------------------------------
languages = ["Python", "Java", "C++"]
print(f"My favorite language is {languages[0]}")

# ---------------------------------
# Example 7: Using f-strings with dictionaries
# ---------------------------------
student = {"name": "Karan", "age": 21}
print(f"Student Name: {student['name']}, Age: {student['age']}")

# ---------------------------------
# Example 8: Multiline f-strings
# ---------------------------------
message = f"""
Student Details:
Name    : {name}
Surname: {surname}
Age     : 21
"""
print(message)

"""
Why use f-strings?
------------------
✔ Cleaner and more readable syntax
✔ Faster than format() and concatenation
✔ Supports expressions and function calls
✔ Preferred way of string formatting in modern Python
"""
