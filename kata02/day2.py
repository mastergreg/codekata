class Chopper:
    def __init__(self, search: int, array: list[int]):
        self.search = search
        self.array = array

    @property
    def left(self):
        return self.array[: len(self.array) // 2]

    @property
    def right(self):
        return self.array[len(self.array) // 2 :]

    def look_left(self):
        if not self.left:
            return False
        return self.left[0] <= self.search <= self.left[-1]

    def look_right(self):
        if not self.right:
            return False
        return self.right[0] <= self.search <= self.right[-1]

    def look(self):
        if self.array and self.array[0] == self.search:
            return 0, []
        if self.look_left():
            return 0, self.left
        if self.look_right():
            return len(self.left), self.right
        return -1, []


def chop(search: int, array_of_number: list[int]):
    array = array_of_number
    tally = 0
    while True:
        chopper = Chopper(search, array)
        _tally, array = chopper.look()
        tally += _tally
        if _tally == -1:
            return _tally
        if not array:
            break
    return tally
