set1 = {1, 2, 3, 4, 5}

# Append new element to set1
buffer_list = list(set1)
buffer_list.append(6)
set1 = set(buffer_list)

set2 = {3, 4, 5, 6, 7, 8}

# set3 is common elements from set1 and set2
set3 = set1 & set2

# transform to list
my_list = list(set3)

print(set1)
print(set2)
print(set3)
print(my_list)
