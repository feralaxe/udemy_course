def merge_list_to_dict(list1, list2):
    return dict(zip(list1, list2))


list_keys = [1, 2, 3, 4, 5]
list_values = ['one', 'two', 'three', 'four', 'five']

# use named arguments
print(merge_list_to_dict(list1=list_keys, list2=list_values))
