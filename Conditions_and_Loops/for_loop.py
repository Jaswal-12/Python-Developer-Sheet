# Python Loops Examples with Explanation

# ------------------------------
# Example 1: Basic for loop with range
# Explanation: range(1,6) generates numbers from 1 to 5.
# The loop prints each number.
for i in range(1, 6):
    print("Number:", i)

print("\n")

# ------------------------------
# Example 2: Using if inside a loop
# Explanation: We check if i is 5, and print a message when the condition is met.
for i in range(1, 11):
    print(i)
    if i == 5:
        print("Halfway done!")

print("\n")

# ------------------------------
# Example 3: Looping through a list
# Explanation: Loop goes through each element in the list 'fruits'.
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print("I like", fruit)

print("\n")

# ------------------------------
# Example 4: Looping through a string
# Explanation: Strings are iterable, so the loop prints each character.
word = "Python"
for letter in word:
    print(letter)

print("\n")

# ------------------------------
# Example 5: Using break in a loop
# Explanation: The loop stops immediately when i equals 6.
for i in range(1, 11):
    if i == 6:
        print("Stop the loop!")
        break
    print(i)

print("\n")

# ------------------------------
# Example 6: Using continue in a loop
# Explanation: continue skips the current iteration for even numbers.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
