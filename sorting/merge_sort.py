def merge_sort(array):
    if len(array) <= 1: return array

    else:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


        return array


data = [66, 1998, 6, 3, 19, 1, 19, -10, -10, 0, 19]
merge_sort(data) # [-10, 1, 3, 6, 19, 66, 1998]
