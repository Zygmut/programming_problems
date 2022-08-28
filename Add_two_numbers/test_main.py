from venv import create
import pytest
from main import *


@pytest.mark.parametrize("input1,input2,expected", [
    ((2,4,3), (5,6,4), [7,0,8]),
    ((0,), (0,), [0]),
    ((9,9,9,9,9,9,9), (9,9,9,9), [8,9,9,9,0,0,0,1])
])
def test_add(input1, input2, expected):
    solution = Solution()
    sol = solution.addTwoNumbers(create_list(input1), create_list(input2))
    values = []
    while sol is not None:
       values.append(sol.val)
       sol = sol.next

    assert values == expected


@pytest.mark.parametrize("input1,input2,expected", [
    (None, [], ValueError),
    (ListNode(), None, ValueError)
])
def test_exceptions_add(input1, input2, expected):
   with pytest.raises(expected):
        sol = Solution()
        sol.addTwoNumbers(input1, input2)


@pytest.mark.parametrize(
    "input,expected",
    [
        ((2, 4, 3), [2, 4, 3]),
        ((5, 6, 4), [5, 6, 4]),
    ],
)
def test_create_list(input, expected):
    data = create_list(input)
    values = []
    while data is not None:
        values.append(data.val)
        data = data.next

    assert values == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((), ValueError),
        ((1, "hola"), ValueError),
        (("hola", 9, 1), ValueError),
        (None, ValueError),
        ([1, 2, 3], ValueError),
        ((1, 10, 0), ValueError),
    ],
)
def test_exceptions_create_list(input, expected):
    with pytest.raises(expected):
        create_list(input)
