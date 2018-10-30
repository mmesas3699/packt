def remove(items, value):
    new_items = []
    found = False
    for item in items:
        # Salta el primer item que sea igual a: value
        if not found and item == value:
            found = True
            continue
        new_items.append(item)

    if not found:
        raise ValueError('list.remove(x): x not in list')

    return new_items


def insert(items, index, value):
    new_items = []
    for i, item in enumerate(items):
        if i == index:
            new_items.append(value)
        new_items.append(item)
    return new_items


items = list(range(10))
print(items)

items = remove(items, 5)
print(items)

items = insert(items, 2, 5)
print(items)

