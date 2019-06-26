lst = [1, 2, 3, 3, 5, 4, 4, 5, 7, 6]


def modify_list(l):
    i = 0
    while i< len(l):
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            i += 1
    for q in range(len(l)):
        l[q] = int(l[q] / 2)

modify_list(lst)
print(lst)