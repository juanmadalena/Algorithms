def bubble_sort(array):
    for i in range(len(array)):

        swapped = False

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped: break
    
    return array

data = [66,-10,1998,6,3,19,1]

bubble_sort(data) # [-10, 1, 3, 6, 19, 66, 1998]