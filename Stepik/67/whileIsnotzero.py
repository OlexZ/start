# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# res 340
whileNotZero = []
res = 0
while True:
    q = int(input())
    whileNotZero.append(q)
    if sum(whileNotZero) == 0:
        break
for i in whileNotZero:
    res += i * i
print(res)