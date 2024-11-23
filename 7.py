def is_prime(func):
    def wrapper(*args):
        func_result = func(*args)
        result = 'Простое'

        for i in range(2, int(func_result ** 0.5)+1):
            if func_result % i == 0:
                result = 'Cоставное'

        print(result)
        return func_result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
