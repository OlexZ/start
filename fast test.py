x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
y = {'a': 6,
     'e': 5, 'f': 6}
del x['d']
z = x.setdefault('g', 7)
x.update(y)
print(x)