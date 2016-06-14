import sys

def sorter(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp

arr = [3, 1, 2, 5, 4]
sorter(arr)

arrLength = len(arr)
for index in range(arrLength):
    print(arr[index], " ")
