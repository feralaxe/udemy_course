list1 = [1, 2, 3]

list2 = [4, 5, 6]

# Common use of + operator
# concatenated_list = list1 + list2

# We will use magic method
concatenated_list = list1.__add__(list2)

# Print the result
print(concatenated_list)
