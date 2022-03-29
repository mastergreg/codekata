def chop_h(search: int, array: list[int], tally: int):
    match array:
        case []:
            return -1
        case [x] if x == search:
            return tally
        case [_]:
            return -1
    left = array[: len(array) // 2]
    right = array[len(array) // 2 :]
    left_search = chop_h(search, left, tally)
    right_search = chop_h(search, right, tally + len(left))
    return max(left_search, right_search)


def chop(search: int, array: list[int]):
    return chop_h(search, array, 0)
