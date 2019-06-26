a = [1, 3, 5, 6, 10]  # [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    a = a * 3
    for i in range(int(len(a) / 3)):
        print(a[i-1] + a[i+1], end=' ')
