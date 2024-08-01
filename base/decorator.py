# def compose(f, g, x):
#     return f(g(x))

# compose(print, len, "Hello, world!")


import random

def random_power():
    def f(x):
        return x ** 2
    
    def g(x):
        return x ** 3
    
    def h(x):
        return x ** 4
    
    functions = [f, g, h]
    return random.choice(functions)

results = []
for i in range(10):
    p = random_power()
    results.append(p(3))
print(results)