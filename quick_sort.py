import random

nums = [random.randint(1,20) for i in range(0, 20)]

print(nums)

def quicksort(arr):
    if len(arr) < 1:
        return []
    pivot = arr.pop()

    big_list= []
    small_list = []
    
    for num in arr:
        if num > pivot:
            big_list.append(num)
        else:
            small_list.append(num)

    return quicksort(small_list) + [pivot] + quicksort(big_list)

snums = quicksort(nums)
print(snums)