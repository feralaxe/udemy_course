#  the use of f-string
def f_string_concat(arg1, arg2):
    return f"{arg1}{arg2}"


print(f_string_concat('concat', 'enate'))


#  args here is a tuple with any number of input parameters
def concat_from_tuple(*args):
    result = str()
    for arg in args:
        result += arg
    return result


print(concat_from_tuple('123', '456', 'test'))


#  args here is a dict with named argumets
def concat_from_dict(**args):
    return f"{args.get('arg1')}{args.get('arg2')}{args.get('arg3')}"


print(concat_from_dict(arg1='test1', arg2='test2', arg3='test3', arg4='123'))
