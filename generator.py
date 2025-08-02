# simple list with loop

my_list = [1, 2, 3, 4, 5]

# Iterate over all items (list example)
for item in my_list:
    print(item)


# with generator function 

def my_generator():
    for x in [1, 2, 3, 4, 5]:
        yield x * 2

for item in my_generator():
    print(item)

