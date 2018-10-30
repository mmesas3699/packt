import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Valores individuales')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
# No muestra el valor de 'c' del diccionario b porque busca en el orden
# en que se creo el objeto

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))

print('"d" in m: {}'.format('d' in m))
