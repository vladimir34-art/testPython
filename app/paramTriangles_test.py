import pytest
from app.triangle import TriangleCalculator, SideException

# набор данных: (a, b, c, ожидаемое)
AREA_CASES = [
    (3.0, 4.0, 5.0, 6.0),      # прямоугольный
    (5.0, 5.0, 5.0, 10.83),    # равносторонний
]

PERIMETER_CASES = [
    (3.0, 4.0, 5.0, 12.0),
    (5.0, 5.0, 5.0, 15.0),
]

TYPE_CASES = [
    (5.0, 5.0, 5.0, "equilateral"),
    (5.0, 5.0, 7.0, "isosceles"),
    (3.0, 4.0, 5.0, "scalene"),
]

INVALID_CASES = [
    (0.5, 4.0, 5.0),   # сторона < 1
    (1.0, 2.0, 10.0),  # не треугольник
]

# Тест площади 
@pytest.mark.parametrize("a,b,c,expected", AREA_CASES)
def test_get_area(a, b, c, expected):
    calc = TriangleCalculator(a, b, c)
    # округление до сотых
    assert calc.get_area() == pytest.approx(expected, rel=1e-2)

# Тест периметров
@pytest.mark.parametrize("a,b,c,expected", PERIMETER_CASES)
def test_get_perimeter(a, b, c, expected):
    calc = TriangleCalculator(a, b, c)
    assert calc.get_perimeter() == expected

# Тест определения типа треугольника
@pytest.mark.parametrize("a,b,c,expected", TYPE_CASES)
def test_get_type(a, b, c, expected):
    calc = TriangleCalculator(a, b, c)
    assert calc.get_type() == expected

# Проверка исключения на неверных данных
@pytest.mark.parametrize("a,b,c", INVALID_CASES)
def test_invalid_sides_raise_exception(a, b, c):
    with pytest.raises(SideException):
        TriangleCalculator(a, b, c)