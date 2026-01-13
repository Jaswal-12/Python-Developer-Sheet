# 🔁 MATCH-CASE IN PYTHON
# ---------------------
# match-case is Python’s version of switch-case.
# It was introduced in Python 3.10.
# It is used to match a variable against multiple values.

x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _:
        print("This is the default case")
