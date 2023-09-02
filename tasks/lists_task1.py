# List with 5 different typed objects
my_list = [1, 'abc', 2.5, ['inner list', 123],
           {1: 'first value', 2: 'second value'}]

# Deletion of 3rd element
my_list.pop(2)

# List length
print(len(my_list))

# reverse list
my_list.reverse()
# my_list = my_list[::-1]  # Another way

# Another list with 2 elements
another_list = ['link', 'name']

# Extention of 1st list without creating new object in memory
my_list.extend(another_list)

# Print the result
print(my_list)
