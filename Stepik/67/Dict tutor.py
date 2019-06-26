d = {'C': 14, 'A': 12, 'T': 9, 'G': 19}
for key in d: # Перебераємо словник по ключам
    print(key, end=' ')

print()
for key in d.keys(): # Перебераємо ключі словника за допомогою метода .keys()
    print(key, end=' ')

print()
for value in d.values(): # Перебераємо значення словника за допомогою метода .values()
    print(value, end=' ')

print()
for key, value in d.items(): # Перебераємо ключ, значення словника за допомогою метода .items()
    print(key, value, end=': ')