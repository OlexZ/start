# a aa abC aa ac abc bcd a
txt = input().lower().split()
resDict = {}
for i in txt:
    if i not in resDict:
        num = txt.count(i)
        resDict.setdefault(i, num)
        print(i + ' ' + str(num))

