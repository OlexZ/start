res = {}
counter = 0
cla = 0
height = 0
for i in range(1,12):
    with open('dataset_3380_5.txt') as f:
        for line in f:
            temp = line.replace('\n', ' ').split()
            if int(temp[0]) == i:
                print(temp)