products = ['chocolate', 'cookies', 'cola', 'ice_cream']
prices = ['10', '8', '5', '12']
availability = [True, True, False, True]

prices_list = list(zip(products, prices))
prices_dict = dict(zip(products, prices))

availability_dict = dict(zip(products, availability))

print(prices_list)
print(prices_dict)
print(availability_dict)
