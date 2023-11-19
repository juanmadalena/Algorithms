def selection_sort(array):

    for x in range(len(array)):
        min_index = x

        for j in range(x+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[x], array[min_index] = array[min_index], array[x]

    return array
        
data = [66, 1998, 6, 3, 19, 1, 19, -10, -10, 0, 19]
selection_sort(data)