"""
File Handling in Python
Author: Karan
Description:
This script demonstrates how to read, write, append, and create files
using different file modes in Python.
"""

# -------------------------------
# Reading a file (r mode)
# -------------------------------

try:
    f = open("myfile.txt", "r")
    text = f.read()
    print("File Content:")
    print(text)
    f.close()
except FileNotFoundError:
    print("Error: File does not exist")

# -------------------------------
# Writing to a file (w mode)
# -------------------------------
# NOTE: This will overwrite existing content

f = open("myfile.txt", "w")
chars_written = f.write("This content is written using write mode.\n")
print(f"\nCharacters written: {chars_written}")
f.close()

# -------------------------------
# Appending to a file (a mode)
# -------------------------------
# NOTE: Content is added at the end

f = open("myfile.txt", "a")
f.write("This line is appended using append mode.\n")
f.close()

# -------------------------------
# Creating a new file (x mode)
# -------------------------------

try:
    f = open("newfile.txt", "x")
    f.write("New file created successfully.")
    f.close()
except FileExistsError:
    print("\nError: File already exists")

# -------------------------------
# Writing to another file example
# -------------------------------

f = open("myfile2.txt", "w")
f.write("Hello, World!")
f.close()

# Appending more content
f = open("myfile2.txt", "a")
f.write("\nHello again!")
f.close()

# -------------------------------
# Using WITH statement (Best Practice)
# -------------------------------
# Automatically closes the file

with open("myfile2.txt", "a") as f:
    f.write("\nWritten using with statement.")

# -------------------------------
# Reading file line by line
# -------------------------------

with open("myfile2.txt", "r") as f:
    print("\nReading file line by line:")
    for line in f:
        print(line.strip())

# -------------------------------
# File Modes Summary
# -------------------------------
"""
r  -> Read only
w  -> Write (overwrite)
a  -> Append
x  -> Create new file
r+ -> Read and write
w+ -> Write and read
a+ -> Append and read
"""
