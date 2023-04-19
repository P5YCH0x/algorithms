def isort(x : list):
    i = 0
    while i < len(x):
        if i > 0 and x[i-1] > x[i]:
            temp = x[i]
            x[i] = x[i-1]
            x[i-1] = temp
            i -= 2
        i += 1
    return x


unsorted_list = [7,5,8,2,8,4,9]

sorted_list = isort(unsorted_list)
print(sorted_list)