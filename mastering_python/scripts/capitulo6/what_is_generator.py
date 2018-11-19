def generator():
    yield 'this is a generator'
    return None

g = generator()
next(g)

