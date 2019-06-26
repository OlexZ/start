
res = []

# 906609

def isPalindrome(palin):
    if palin == palin[::-1]:
        return True


for a in range(1000, 100, -1):
    for b in range(1000, 100, -1):
        if isPalindrome(str(a * b)) == True:
            res.append(a * b)
            break

print(max(res))
