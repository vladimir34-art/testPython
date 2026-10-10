import sys
import os
# Добавляем корень проекта в путь, чтобы видеть папку app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.triangle import TriangleCalculator, SideException
import pytest
from app.triangle import TriangleCalculator, SideException

def test_classic_triangle():
    assert TriangleCalculator(3, 4, 5).get_area() == 6.0

def test_equilateral_on_lower_bound():
    assert TriangleCalculator(1, 1, 1).get_area() == pytest.approx(0.43)

def test_permutation_same_result():
    assert TriangleCalculator(5, 3, 4).get_area() == 6.0

def test_side_below_min():
    with pytest.raises(SideException, match="Стороны должны быть от 1 до 100"):
        TriangleCalculator(0.99, 1, 1).get_area()

def test_side_at_max_boundary():
    with pytest.raises(SideException, match="Стороны должны быть от 1 до 100"):
        TriangleCalculator(100, 50, 50).get_area()

def test_non_existent_triangle():
    with pytest.raises(SideException, match="Недопустимые длины сторон"):
        TriangleCalculator(1, 1, 2.5).get_area() 
        