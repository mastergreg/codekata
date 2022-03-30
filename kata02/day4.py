def chop(search: int, array: list[int]):
    left = 0
    right = len(array) - 1
    while left <= right:
        pivot = (left + right) // 2
        if array[pivot] < search:
            left = pivot + 1
        elif array[pivot] > search:
            right = pivot - 1
        else:
            return pivot
    return -1
