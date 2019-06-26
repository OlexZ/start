a = [4, 8, 0, 3, 4, 2, 0, 3]#[int(i) for i in input().split()]
res = []
for i in a:
    if a.count(i) > 1 and i not in res:
        print(i, end=" ")
        res += [i]