count = 0
res = 0
data = [1, 2, 3]

def multi(data):
    global count
    global res
    if count < len(data):
        res += data[count]
        count += 1
        multi(data)
    return res


def checkio(data):
    if len(data) == 1:
        return data[0]
    global count
    global res
    resultatOfMultiply = multi(data)
    count = 0
    res = 0
    return resultatOfMultiply


print(checkio(data))
