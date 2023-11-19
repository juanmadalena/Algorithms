def insertion_sort(array):

    for step in range(1,len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    
    return array

data = [66,-10,1998,6,3,19,1]

insertion_sort(data)