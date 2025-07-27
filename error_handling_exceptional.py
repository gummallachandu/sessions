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

# Step 1: Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative numbers not allowed: {value}")

# Step 2: Function that raises the custom error
def square_root(x):
    if x < 0:
        raise NegativeNumberError(x)
    return x ** 0.5

# Step 3: Use try-except to handle it
try:
    num = -9
    result = square_root(num)
    print(f"Square root is: {result}")
except NegativeNumberError as e:
    print(f"Custom Error: {e}")

