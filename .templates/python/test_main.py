import pytest


@pytest.mark.parametrize(
    "problem,expected",
    (),
)
def test_main(problem, expected):
    pass


@pytest.mark.parametrize(
    "problem,expected",
    (),
)
def test_exceptions_main(problem, expected):
    with pytest.raises(expected):
        pass
