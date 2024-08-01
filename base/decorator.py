def compose(f, g, x):
    return f(g(x))

compose(print, len, "Hello, world!")
