def chop_h(search: int, array: list[int], tally: int) -> int:
    match array:
        case []:
            return -1
        case [x] if x == search:
            return tally
        case [_]:
            return -1
        case _:
            pass
    mid = len(array) // 2
    pivot = array[mid]
    if search >= pivot:
        right = array[mid:]
        return chop_h(search, right, tally + mid)
    else:
        left = array[:mid]
        return chop_h(search, left, tally)


def chop(search: int, array: list[int]):
    return chop_h(search, array, 0)
