# Lists – Indexing, Slicing, Methods (append(), pop())
# Ordered, mutable collections. Indexing starts at 0; slicing with [start:end:step].
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # [2, 3, 4] (slicing)

my_list.append(6)  # [1,2,3,4,5,6]
print(my_list.pop())  # 6, list now [1,2,3,4,5]

# Tuples – Immutable Lists
# Ordered, immutable (can't change after creation).
my_tuple = (1, "apple", True)
print(my_tuple[1])  # "apple"
# my_tuple[0] = 2  # Error: immutable

# Sets – Unique Unordered Collection
# Unordered, unique elements; great for deduplication.
my_set = {1, 2, 2, 3}  # {1,2,3} (duplicates removed)
my_set.add(4)  # {1,2,3,4}
print(2 in my_set)  # True

# Dictionaries – Key-Value Pairs
# Unordered (pre-3.7), mutable mappings.

#Notes: Essential for AI configs (e.g., model params) or JSON-like data
my_dict = {"name": "Bob", "age": 25}
print(my_dict["name"])  # "Bob"
my_dict["city"] = "NY"  # Add key
