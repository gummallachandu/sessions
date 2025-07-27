# Functions and Scope
# Defining functions with def
# Reusable code blocks.
def greet(name):
    print(f"Hello, {name}!")
greet("Charlie")  # Hello, Charlie!

# Arguments: positional, keyword, default, *args, **kwargs
# Flexible parameter passing.

def func(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

func(1, 3, 4, 5, key="value")  # 1 3 (4,5) {'key': 'value'}

# Return statements
# Functions return values (default None).
def multiply(x, y):
    return x * y
result = multiply(3, 4)  # 12

# Variable Scope: local, global
# Local vars inside functions; global outside.
global_var = 10

def test():
    local_var = 5
    global global_var
    global_var += 1
    print(local_var)  # 5

test()
print(global_var)  # 11
