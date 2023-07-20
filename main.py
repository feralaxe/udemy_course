list = [1, 2, 3, 4, 5]

other_list = list

print(list)
print(other_list)
print(id(list))
print(id(other_list))

list.pop()
other_list.pop()

print(list)
print(other_list)
print(id(list))
print(id(other_list))
