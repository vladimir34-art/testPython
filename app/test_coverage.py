import math
import pytest
from app.triangle import TriangleCalculator, SideException

# ветка 1: нормальный расчёт площади
def test_get_area_normal():
    assert TriangleCalculator(3.0, 4.0, 5.0).get_area() == pytest.approx(6.0, rel=1e-2)

# ветка 2: сторона вне диапазона
def test_side_too_small():
    with pytest.raises(SideException):
        TriangleCalculator(0.5, 4.0, 5.0).get_area()

# ветка 3: не выполняется неравенство треугольника
def test_not_a_triangle():
    with pytest.raises(SideException):
        TriangleCalculator(1.0, 2.0, 10.0).get_area()

# ветка 4: except ValueError — подмена math.sqrt, для ошибки
def test_value_error_branch(monkeypatch):
    def fake_sqrt(x):
        raise ValueError("math domain error")
    monkeypatch.setattr(math, "sqrt", fake_sqrt)
    with pytest.raises(SideException):
        TriangleCalculator(3.0, 4.0, 5.0).get_area()

# периметр
def test_perimeter():
    assert TriangleCalculator(3.0, 4.0, 5.0).get_perimeter() == 12.0

# тип треугольника
def test_type():
    assert TriangleCalculator(5.0, 5.0, 5.0).get_type() == "equilateral"
    assert TriangleCalculator(5.0, 5.0, 7.0).get_type() == "isosceles"
    assert TriangleCalculator(3.0, 4.0, 5.0).get_type() == "scalene"