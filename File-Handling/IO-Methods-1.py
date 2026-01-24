"""
FILE HANDLING IN PYTHON
----------------------
This program explains and demonstrates:

1. Reading a file line by line using readline()
2. Writing multiple lines using writelines()
3. Appending multiple lines using writelines()
4. Proper use of try-except and with statement

Author: Karan
"""

# ==========================================================
# 1. Reading a file line by line using readline()
# ==========================================================
# readline() reads ONE line at a time from the file.
# When the end of file (EOF) is reached, it returns an empty string "".

try:
    # Open file in read mode
    f = open("myfile.txt", "r")

    print("Reading file using readline():\n")

    while True:
        line = f.readline()   # Read one line

        # If line is empty, EOF has been reached
        if not line:
            break

        # strip() removes extra newline (\n) from the end
        print(line.strip())

    # Always close the file after use
    f.close()

except FileNotFoundError:
    # This block executes if the file does not exist
    print("Error: myfile.txt does not exist")

# ==========================================================
# 2. Writing multiple lines using writelines()
# ==========================================================
# writelines() writes a LIST of strings to a file.
# It does NOT add newline characters automatically.
# We must add '\n' manually.

print("\nWriting multiple lines using writelines()...")

lines = [
    "Line 1 written using writelines()\n",
    "Line 2 written using writelines()\n",
    "Line 3 written using writelines()\n"
]

# Open file in write mode ('w')
# If file exists -> content is overwritten
# If file does not exist -> file is created
with open("myfile2.txt", "w") as f:
    f.writelines(lines)

print("Lines written successfully")

# ==========================================================
# 3. Appending multiple lines using writelines()
# ==========================================================
# Append mode ('a') adds content at the END of the file
# Existing data is not removed

print("\nAppending lines using writelines()...")

extra_lines = [
    "Extra Line 1 appended\n",
    "Extra Line 2 appended\n"
]

with open("myfile2.txt", "a") as f:
    f.writelines(extra_lines)

print("Lines appended successfully")

# ==========================================================
# 4. Why use WITH statement?
# ==========================================================
# - Automatically closes the file
# - Cleaner and safer code
# - Recommended best practice

print("\nProgram completed successfully.")
