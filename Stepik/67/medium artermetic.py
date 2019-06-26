a, b = (int(i)for i in input().split())
count = 0
res = 0
for i in range(a, b + 1,):
    if i % 3 == 0:
        count += 1
        res += i
print(res / count)
