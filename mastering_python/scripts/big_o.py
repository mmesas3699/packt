def o_one(items):
    return 1  # 1 operation so O(1)


def o_n(items):
    total = 0
    # Recorre todos los items, entonces O(n)
    for item in items:
        total += item
    return total


def o_n_squared(items):
    total = 0
    # Recorre todos los itmes n*n veces, entonces O(n**2)
    for a in items:
        for b in items:
            total += a * b
    return total


n = 10
items = range(n)
o_one(items)  # 1 operacion
o_n(items)  # n = 10 operaciones
o_n_squared(items)  # n*n = 10*10 = 100 operaciones

