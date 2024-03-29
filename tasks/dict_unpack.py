dict1 = {'key1': 'value1',
         'key2': 'value2',
         'key3': 'value3'}

dict2 = {'key4': 'value4',
         'key1': 'value1'}

dict1_ext = {**dict1,
             'key5': 'value5'}

print(dict1_ext)

dict_union = dict1 | dict2

print(dict_union)

dict2_replaced_val = {**dict2,
                      'key4': 'value4_replaced'}

print(dict2)
print(dict2_replaced_val)
