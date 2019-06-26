st = 'aaaaaaaaaaaaaaaaaaaabbbbbccccccccccccccccccccccccc'
counter = 0
res = st[0]
now = st[0]
for i in st:
    if i == res[-1]:
        counter += 1
    else:
        now += str(counter)
        now += i
        res += i
        counter = 1
now += str(counter)
print(now)
