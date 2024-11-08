NUMBERS = [6, 20, 15, 9]


def apply_all_func(int_list, *functions):
    result = dict()
    for func in functions:
        result[func.__name__] = func(int_list)

    return result


print(apply_all_func(NUMBERS, max, min))
print(apply_all_func(NUMBERS, len, sum, sorted))
