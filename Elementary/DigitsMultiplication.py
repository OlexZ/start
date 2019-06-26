a = 1111
b = list(str(a))
print(b)
q = 1
for i in b:
    if int(i) == 0:
        continue
    else:
        q *= int(i)
print(q)


