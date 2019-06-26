a, b, c, d = (int(i)for i in input().split())


for q in range(c, d + 1):
    print('\t' + str(q), end='')
print()

for i in range(a, b + 1):
    print(str(i), end='')
    for j in range(c, d + 1):
        print('\t' + str(i*j), end='')
    print()