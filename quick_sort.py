from cmath import pi
import random

nums = [random.randint(1,20) for i in range(0, 10)]

print(nums)
print(len(nums))

def quicksort(arr):
    if len(arr) < 1:
        return []
    pivot = arr.pop()

    biglist= []
    smalllist = []
    
    for num in arr:
        if num > pivot:
            biglist.append(num)
        else:
            smalllist.append(num)

    return quicksort(biglist) + [pivot] + quicksort(smalllist)

snums = quicksort(nums)
print(len(snums))
print(snums)