def chop(search: int, array_of_number: list[int]):
    array = array_of_number
    tally = 0
    while True:
        if len(array) > 1:
            left = array[: len(array) // 2]
            right = array[len(array) // 2 :]
            if search >= right[0]:
                tally += len(left)
                array = right
            else:
                array = left
        elif array and search == array[0]:
            return tally
        else:
            return -1
