res = {}
counter = 0
height = 0
for i in range(1,12):
    with open('dataset_3380_5.txt') as f:
        for line in f:
            temp = line.replace('\n', ' ').split()
            if int(temp[0]) == i:
                height += int(temp[2])
                counter += 1
        if height != 0:
            res.setdefault(i, float(height / counter))
        else:
            res.setdefault(i, '-')
        height = 0
        counter = 0
for key, values in res.items():
    print(key, values)