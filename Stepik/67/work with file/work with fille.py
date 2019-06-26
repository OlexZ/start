# a3b4c2e10b1
# aaabbbbcceeeeeeeeeeb

with open('dataset_3363_2.txt') as a:
    txt = a.readline().strip()
num = ''
res = ''
caunter = 1
for i in txt:
    if i.isdecimal():
       num += str(i)
    else:
        num += " "
num = num.split(" ")
for j in txt:
    if j.isalpha():
        res += j * int(num[caunter])
        caunter += 1
with open('dataset_3363_2.txt', 'w') as b:
    b.write(res + '\n')

# from re import sub
#
# with open('in.txt', 'r') as in_f, open('out.txt', 'w') as out_f:
#  s = in_f.readline()
#  letters = [x for x in s if x.isalpha()]
#  numbers = sub('[a-zA-Z]', ' ', s).split()
#
#  for x in range(len(letters)):
#   out_f.write(letters[x] * int(numbers[x]))