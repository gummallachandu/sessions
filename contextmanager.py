
file = open('datasets/delhivery_data.csv', 'r')
try:
    first_line = file.readline()
    print(first_line.strip())
finally:
    file.close()  # You must remember to close the file!




# Using 'with' as a context manager for files
with open('datasets/delhivery_data.csv', 'r') as file:
    first_line = file.readline()
    print(first_line.strip())

# After the 'with' block, the file is automatically closed—even if an exception was raised.
