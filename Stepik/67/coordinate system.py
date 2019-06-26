x, y = 0, 0
# coordinate = {key: value for key, value in (input().split() for _ in range(num))}
# coordinate = {'север': "10",
#               'запад': "10",
#               'юг': "10",
#               'восток': "10"}
for i in range(int(input())):
    coordinate = input().split()
    if coordinate[0] == 'север':
        y += int(coordinate[1])
    elif coordinate[0] == 'запад':
        x -= int(coordinate[1])
    elif coordinate[0] == 'юг':
        y -= int(coordinate[1])
    else:
        x += int(coordinate[1])
print(x, y)
