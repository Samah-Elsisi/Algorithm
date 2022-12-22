def mergesort(array, start, end):
    
    if end - start > 1:
        mid = (start + end)//2
        mergesort(array, start, mid)
        mergesort(array, mid, end)
        mergelist(array, start, mid, end)
 
def mergelist(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1
 
 
array = input('Enter the array of numbers: ').split()
array = [int(x) for x in array]
mergesort(array, 0, len(array))
print('Sorted array: ', end='')
print(array)