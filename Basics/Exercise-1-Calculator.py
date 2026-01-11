# Simple Calculator Program

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation (+, -, *, /, %): ")

# Performing calculation
if c == "+":
    print("Result:", a + b)

elif c == "-":
    print("Result:", a - b)

elif c == "*":
    print("Result:", a * b)

elif c == "/":
    print("Result:", a / b)

elif c == "%":
    print("Result:", a % b)

else:
    print("Invalid operation!")
