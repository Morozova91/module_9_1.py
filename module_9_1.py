# Задача "Вызов разом"

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)

    return results


def min_list(list):
    return min_list(list)


def max_list(list):
    return max_list(list)


def len_list(list):
    return len_list(list)


def sum_list(list):
    total = 0
    for x in list:
        total += x
    return total


def sorted_list(list):
    return sorted(list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))