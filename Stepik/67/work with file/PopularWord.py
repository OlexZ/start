# abc a bCd bC AbC BC BCD bcd ABC
# abc 3
with open('dataset_3363_3.txt', 'r') as a:
    txt = a.read().strip().lower().split()
resStr = ''
resNum = 0
for i in txt:
    if txt.count(i) > resNum:
        resStr = i
        resNum = txt.count(i)
with open('dataset_3363_3.txt', 'w') as b:
    b.write(resStr + ' ' + str(resNum) + '\n')


# with open('in.txt', 'r') as in_f, open('out.txt', 'w') as out_f:
#  l, d = ''.join(in_f.readlines()).lower().split(), {}
#  
#  for x in set(l):
#   d.update({l.count(x): x})
#  
#  print(d[max(d)], max(d))