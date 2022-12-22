def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while (j >= 0 and key < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
 
 
array = input('Enter the array of numbers: ').split()
array = [int(x) for x in array]
insertionsort(array)
print('Sorted array: ', end='')
print(array)