import pytest
import day1


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
def test_chop(expected, test_input):
    assert day1.chop(*test_input) == expected
