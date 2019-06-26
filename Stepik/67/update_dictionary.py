d = dict()


def update_dictionary(d, key, value):
    if key in d: # чи є ключ в словнику якщо є добавити до ключа ще одне значення
        d[key].append(value)
    elif (2 * key) in d:        # якщо ключа немає, два множимо на ключ і провіряємо чи є такий ключ
        d[2 * key].append(value)
    else:                       # якщо і такого немає створюємо цей ключ з значенням
        d.setdefault(2*key, [value])



print(d)
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
# update_dictionary(d, 2, 4)
# print(d)
#
#  Best Solution
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     else:
#         d.setdefault(2*key,[]).append(value)