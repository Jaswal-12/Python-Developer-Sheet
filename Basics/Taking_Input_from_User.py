# ============================================
#  User Input in Python
#  Python Developer Sheet
# ============================================

# Example 1: Taking a name from user
name = input("Enter your name: ")
print("My name is", name)

print("----------------------------------")

# Example 2: input() always returns string
x = input("Enter a number: ")
print("You entered:", x)
print("Data type of x:", type(x))

print("----------------------------------")

# Example 3: Converting input to integer
age = int(input("Enter your age: "))
print("Your age is:", age)
print("Data type of age:", type(age))

print("----------------------------------")

# Example 4: Taking two numbers and adding them (Wrong way)
a = input("Enter first number: ")
b = input("Enter second number: ")
print("Without type conversion:", a + b)

print("----------------------------------")

# Example 5: Taking two numbers and adding them (Correct way)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("With type conversion (Sum):", a + b)

print("----------------------------------")

# Example 6: Taking float input
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
print("Total cost:", price * quantity)

print("----------------------------------")

# Example 7: Taking multiple inputs in one line
x, y = map(int, input("Enter two numbers (space separated): ").split())
print("Sum of two numbers:", x + y)

print("----------------------------------")
