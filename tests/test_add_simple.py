import pytest
from src.math_utils import add_number

@pytest.fixture(params=[
        ([5, 8], 13),           # два положительных
        ([-2, 11, 5, -7], 7),   # разные знаки, 4 числа
        ([0, 0, 0], 0),         # только нули
        ([9, -9], 0),           # равно ноль
        ([0, 6, 0], 6),         # c нулями
        ([1, 3, 4, 6, 10], 24), # только положительные
])
def test_case(request):
    return request.param

def test_add_with_fixture(test_case):
    numbers, expected = test_case
    result = add_number(*numbers)
    assert result == expected