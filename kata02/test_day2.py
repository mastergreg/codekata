import pytest
import day2


@pytest.mark.parametrize(
    "expected, test_input",
    [
        (-1, (3, [])),
        (-1, (3, [1])),
        (0, (1, [1])),
        (1, (3, [1, 3, 5])),
        (2, (5, [1, 3, 5])),
        (-1, (0, [1, 3, 5])),
        (-1, (2, [1, 3, 5])),
        (-1, (4, [1, 3, 5])),
        (-1, (6, [1, 3, 5])),
        (0, (1, [1, 3, 5, 7])),
        (1, (3, [1, 3, 5, 7])),
        (2, (5, [1, 3, 5, 7])),
        (3, (7, [1, 3, 5, 7])),
        (-1, (0, [1, 3, 5, 7])),
        (-1, (2, [1, 3, 5, 7])),
        (-1, (4, [1, 3, 5, 7])),
        (-1, (6, [1, 3, 5, 7])),
        (-1, (8, [1, 3, 5, 7])),
    ],
)
def test_chop_day2(expected, test_input):
    assert day2.chop(*test_input) == expected


@pytest.mark.parametrize(
    "expected, test_input",
    [
        ([], (3, [])),
        ([], (3, [1])),
        ([], (1, [1])),
        ([1], (3, [1, 3, 5])),
        ([1], (5, [1, 3, 5])),
        ([1], (0, [1, 3, 5])),
        ([1], (2, [1, 3, 5])),
        ([1], (4, [1, 3, 5])),
        ([1], (6, [1, 3, 5])),
        ([1, 3], (1, [1, 3, 5, 7])),
        ([1, 3], (3, [1, 3, 5, 7])),
        ([1, 3], (5, [1, 3, 5, 7])),
        ([1, 3], (7, [1, 3, 5, 7])),
        ([1, 3], (0, [1, 3, 5, 7])),
        ([1, 3], (2, [1, 3, 5, 7])),
        ([1, 3], (4, [1, 3, 5, 7])),
        ([1, 3], (6, [1, 3, 5, 7])),
        ([1, 3], (8, [1, 3, 5, 7])),
    ],
)
def test_chopper_left(expected, test_input):
    chopper = day2.Chopper(*test_input)
    assert chopper.left == expected


@pytest.mark.parametrize(
    "expected, test_input",
    [
        ([], (3, [])),
        ([1], (3, [1])),
        ([1], (1, [1])),
        ([3, 5], (3, [1, 3, 5])),
        ([3, 5], (5, [1, 3, 5])),
        ([3, 5], (0, [1, 3, 5])),
        ([3, 5], (2, [1, 3, 5])),
        ([3, 5], (4, [1, 3, 5])),
        ([3, 5], (6, [1, 3, 5])),
        ([5, 7], (1, [1, 3, 5, 7])),
        ([5, 7], (3, [1, 3, 5, 7])),
        ([5, 7], (5, [1, 3, 5, 7])),
        ([5, 7], (7, [1, 3, 5, 7])),
        ([5, 7], (0, [1, 3, 5, 7])),
        ([5, 7], (2, [1, 3, 5, 7])),
        ([5, 7], (4, [1, 3, 5, 7])),
        ([5, 7], (6, [1, 3, 5, 7])),
        ([5, 7], (8, [1, 3, 5, 7])),
    ],
)
def test_chopper_right(expected, test_input):
    chopper = day2.Chopper(*test_input)
    assert chopper.right == expected


@pytest.mark.parametrize(
    "expected, test_input",
    [
        (False, (3, [])),
        (False, (3, [1])),
        (False, (1, [1])),
        (False, (3, [1, 3, 5])),
        (False, (5, [1, 3, 5])),
        (False, (0, [1, 3, 5])),
        (False, (2, [1, 3, 5])),
        (False, (4, [1, 3, 5])),
        (False, (6, [1, 3, 5])),
        (True, (1, [1, 3, 5, 7])),
        (True, (3, [1, 3, 5, 7])),
        (False, (5, [1, 3, 5, 7])),
        (False, (7, [1, 3, 5, 7])),
        (False, (0, [1, 3, 5, 7])),
        (True, (2, [1, 3, 5, 7])),
        (False, (4, [1, 3, 5, 7])),
        (False, (6, [1, 3, 5, 7])),
        (False, (8, [1, 3, 5, 7])),
    ],
)
def test_chopper_look_left(expected, test_input):
    chopper = day2.Chopper(*test_input)
    assert chopper.look_left() == expected


@pytest.mark.parametrize(
    "expected, test_input",
    [
        (False, (3, [])),
        (False, (3, [1])),
        (True, (1, [1])),
        (True, (3, [1, 3, 5])),
        (True, (5, [1, 3, 5])),
        (False, (0, [1, 3, 5])),
        (False, (2, [1, 3, 5])),
        (True, (4, [1, 3, 5])),
        (False, (6, [1, 3, 5])),
        (False, (1, [1, 3, 5, 7])),
        (False, (3, [1, 3, 5, 7])),
        (True, (5, [1, 3, 5, 7])),
        (True, (7, [1, 3, 5, 7])),
        (False, (0, [1, 3, 5, 7])),
        (False, (2, [1, 3, 5, 7])),
        (False, (4, [1, 3, 5, 7])),
        (True, (6, [1, 3, 5, 7])),
        (False, (8, [1, 3, 5, 7])),
    ],
)
def test_chopper_look_right(expected, test_input):
    chopper = day2.Chopper(*test_input)
    assert chopper.look_right() == expected
