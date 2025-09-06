from copy import deepcopy

my_dict = {'key1': 'value1',
           'key2': 'value2',
           'list1': ['list_value1', 'list_value2']}

my_dict['other_key'] = 'other_value'

my_dict_shallow_copy = my_dict.copy()

my_dict_shallow_copy['list1'].append('list_value3')
my_dict_shallow_copy['list1'].append('list_value4')
my_dict_shallow_copy['list1'].append('list_value5')

# print(my_dict)
# print(my_dict_shallow_copy)

my_dict_deep_copy = deepcopy(my_dict)

my_dict_deep_copy['list1'].append('list_value4')
my_dict_deep_copy['another_key'] = 'another_value'

print(my_dict)
print(my_dict_shallow_copy)
print(my_dict_deep_copy)
