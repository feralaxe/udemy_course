inp_dict = {}

num_of_pairs = 3

while num_of_pairs >= 1:

    input_key = input('Enter key: ')
    input_value = input('Enter value: ')

    inp_dict[input_key] = input_value

    num_of_pairs -= 1

print(inp_dict)
