

# Reading from the file without 'with'
file = open("example.txt", "r")  # Open in read mode
content = file.read()  # Read content
print(content)  # Output: Hello, world!
file.close()  # Manually close    

# 8️⃣ Working with Files
# Reading and Writing Text Files
# Use open() to read ('r') or write ('w') text files. Read with read() or readlines(); write with write().

# Notes: Files are strings by default. Close files manually if not using with.

# This is safer and cleaner—the file auto-closes after the block, handling exceptions gracefully.

# Writing
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Reading
with open("example.txt", "r") as file:
    content = file.read()
print(content)  # Hello, world!

# Context Manager with 'with open()'
# The with statement auto-closes files, preventing leaks.

# Notes: Safer for AI scripts handling large datasets.


with open("example.txt", "a") as file:  # Append mode
    file.write("\nNew line added.")
    
with open("example.txt", "r") as file:
    lines = file.readlines()  # List of lines
print(lines)  # ['Hello, world!\n', 'New line added.']

# CSV/JSON File Handling Basics
# Use csv module for CSV; json for JSON. Read/write structured data.

# Notes: CSV for tabular data (e.g., AI datasets); JSON for APIs.

# Example (Assume imports: import csv, json):

# CSV Write/Read
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Name', 'Age'], ['Alice', '30'], ['Bob', '25']

# JSON Write/Read
json_data = {"name": "Alice", "age": 30}
with open("data.json", "w") as file:
    json.dump(json_data, file)

with open("data.json", "r") as file:
    loaded = json.load(file)
print(loaded["name"])  # Alice
