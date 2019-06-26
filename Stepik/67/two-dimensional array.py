n = 3
a = [[0] * n for i in range(n)]
a[0][2] = 5
print(a)
b = [[0 for j in range(n)] for i in range(n)]
b[0][1] = 6
print(b)
