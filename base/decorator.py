# def compose(f, g, x):
#     return f(g(x))

# compose(print, len, "Hello, world!")


# import random

# def random_power():
#     def f(x):
#         return x ** 2
    
#     def g(x):
#         return x ** 3
    
#     def h(x):
#         return x ** 4
    
#     functions = [f, g, h]
#     return random.choice(functions)

# results = []
# for i in range(10):
#     p = random_power()
#     results.append(p(3))
# print(results)


# import time


# def prime_factorization(n):
#     start_time = time.time()
#     factors = []
#     divisor = 2

#     while n > 1:
#         while n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         divisor += 1
    
#     stop_time = time.time()
#     print(f'time_diff = {stop_time - start_time}')
#     return factors

# integers = [2**20+1, 2**23+1, 2*29+1, 2**32+1]
# for num in integers:
#     factorization = prime_factorization(num)
#     print(f'Prime factorization of {num} = {factorization}')
#     print(20*'=')


import time


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time
        dt = stop_time - start_time
        print(f'diff_time = {dt}')
        return result
    
    return wrapper



def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors