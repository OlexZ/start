array = [int(i) for i in input().split()]
num = int(input())
if num not in array:
    print("Отсутствует")
else:
    for i in range(len(array)):
        if num == array[i]:
            print(i, end=" ")
