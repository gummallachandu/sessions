Python Syntax and Data Types
Variables and Data Types (int, float, str, bool)
Variables are dynamically typed and assigned without declaration. Basic types: int (integers), float (decimals), str (strings), bool (True/False).

Notes: In AI, use float for model weights, str for text data, bool for flags (e.g., training mode).

age = 30  # int
height = 5.9  # float
name = "Alice"  # str
is_student = False  # bool

print(f"{name} is {age} years old, height {height} ft, student: {is_student}")


# size of the variables 
import sys
x = 42
y = "hello"
print(sys.getsizeof(x))  # ~28 bytes
print(sys.getsizeof(y))  # ~54 bytes (40 + 5 chars + overhead)

#inputs 
user_input = input("Enter your name: ")  # Reads from console
print(f"Hello, {user_input}!")  # Formatted output

