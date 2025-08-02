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
