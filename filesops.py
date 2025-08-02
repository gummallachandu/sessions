Why is a Context Manager Important?
Automatic Resource Management: Ensures resources (like open files) are released promptly and reliably, even if an error or exception occurs.

Prevents Resource Leaks: If you forget to call .close(), resources might remain open, leading to memory leaks, file corruption, or locked files.

Cleaner, More Readable Code: Using with makes your code easier to read and maintain, reducing the chance of bugs.

Exception Safety: The file (or other resource) is always closed properly—even if something goes wrong inside the block.

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


def read_in_chunks(file_path, chunk_size=1024):  # Generator function
    with open(file_path, "rb") as file:  # Binary mode for any file type
        while True:
            chunk = file.read(chunk_size)  # Read fixed-size chunk
            if not chunk:  # End of file
                break
            yield chunk  # Yield (return lazily) without storing

# Usage: Process chunks lazily
for chunk in read_in_chunks("large_file.bin", chunk_size=4096):  # 4KB chunks
    print(len(chunk))  # Process chunk (e.g., analyse or upload to AI model)
