import random


def findPeak(arr):
    if arr[0] > arr[1]:     # check left corner
        return arr[0]

    elif arr[-1] > arr[-2]:     # check right corner
        return arr[-1]
        
    else:                       # check the rest of array
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return arr[i]




myNums = [random.randint(0, 100) for i in range(0, 10)]

print(myNums)
print(findPeak(myNums))