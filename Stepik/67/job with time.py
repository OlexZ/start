a = int(input())
hours = int(input())
minutes = int(input())
h = a//60 + hours
m = a%60 + minutes
if m > 59:
    m -= 60
    h += 1

print(h)
print(m)