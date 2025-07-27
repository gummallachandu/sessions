# try, except, finally blocks
# Handle errors gracefully.
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup done.")  # Always runs

# Common Exceptions
# e.g., ValueError, TypeError, IndexError, KeyError.
try:
    int("abc")  # ValueError
except ValueError as e:
    print(f"Error: {e}")  # Error: invalid literal for int() with base 10: 'abc'

# Raising Exceptions
# Manually throw errors with raise.

def check_positive(n):
    if n < 0:
        raise ValueError("Number must be positive!")
    return n

try:
    check_positive(-1)
except ValueError as e:
    print(e)  # Number must be positive!
