#Iterates over a sequence (like a list, tuple, string, or range) for a fixed number of times.

for i in range(5):  # Loops 0 to 4
    print(i)

#While Loop: Repeats as long as a condition is true, suitable for indeterminate iterations
count = 0
while count < 5:  # Loops until count reaches 5
    print(count)
    count += 1

# terates directly over elements in a list.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Uses range() to generate a sequence of numbers for looping a specific number of times.

for i in range(3):  # 0 to 2
    print(i * 2)

#With Start and Step:

for i in range(1, 6, 2):  # Start at 1, stop before 6, step by 2
    print(i)

#Iterating Over a String

for char in "Hello":
    print(char)

# Using enumerate() for Index and Value
# Provides both the index and value of each item in a sequence.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):  # Start index at 1
    print(f"{index}: {color}")

#Iterating Over Dictionary
#Can loop over keys, values, or key-value pairs using .items().
car = {"brand": "Subaru", "model": "Model Y", "year": 2025}
for key, value in car.items():
    print(f"{key}: {value}")

for key in car.keys():
    print(key)

for value in car.values():
    print(value)

# nested loops
matrix = [[1, 2], [3, 4]]
# Current date and time: 10:39 PM EDT on Saturday, July 26, 2025

print("*** Starting outer loop, row =", matrix[0])  # Step 1: Begin first row
for row in matrix:
    print("*** Entering inner loop for row =", row)  # Step 2: Start inner loop
    for item in row:
        print("*** Printing item =", item, end=" ")  # Step 3: Print each item
    print("*** Finished inner loop, moving to next line")  # Step 4: End of row
    print()  # New line after each row
print("*** Completed all loops")  # Step 5: End of execution
