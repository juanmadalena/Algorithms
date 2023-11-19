def binary_search(array, num_to_find, left = 0, right = -1):

    if right == -1 : right = len(array) - 1

    if left <= right: 

        mid = (left + right) // 2

        if num_to_find == array[mid]:
            return mid

        elif array[mid] < num_to_find:
            return binary_search(array, num_to_find, mid + 1, right)


        else:
            return binary_search(array, num_to_find, left, mid - 1)
    
    else:
        return -1


data = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(data, 3))