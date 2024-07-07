def apply_all_func(int_list,*function):
    result = {}
    function_list = function
    for action in function_list:
        result[action.__name__] = action(int_list)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))