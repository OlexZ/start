def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    bq = range(1, len(arr))
    for q in bq:  # range numbers from 1 and length massive
        if arr[q] < smallest:
            smallest = arr[q]
            smallest_index = q
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 9, 10]))
