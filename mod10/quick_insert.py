def find_insert_position(array, num):
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < num:
            left = middle + 1
        else:
            right = middle
    return left
