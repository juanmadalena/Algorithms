def quick_sort(array):
    if len(array) <= 1: return array
    else:
        pivot = array[ len(array) // 2 ]
        array.remove(pivot)
        # num less than pivot
        less = [x for x in array if x <= pivot]
        # num greater than pivot
        greater = [x for x in array if x > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


data = [66, 1998, 6, 3, 19, 1, 19, -10, -10, 0, 19]
quick_sort(data) # [-10, 1, 3, 6, 19, 66, 1998]