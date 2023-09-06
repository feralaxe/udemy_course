def update_car_info(**args):
    if not args.get('is_avaliable'):
        args['is_avaliable'] = True
    return args


updated_car_info = update_car_info(brand='Toyota', price='30000')
print(updated_car_info)
