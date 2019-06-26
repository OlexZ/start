my_list = []

i = 1
while i <= 40000000:
    my_list.append(i)
    i += 1


def binary_search(list, item):
    count = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            print(str(count) + "  - Кількість ітерацій")
            return mid
        if guess > item:
            high = int(mid - 1)
        else:
            low = int(mid + 1)
    return None


# print(my_list)
res = binary_search(my_list, 1)
print(my_list[int(res)])

