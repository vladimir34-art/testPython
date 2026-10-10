import unittest
from app.triangle import TriangleCalculator, SideException

class TestPositiveTriangle(unittest.TestCase):
    # позитивные тесты

    def test_classic_triangle(self):
        calc = TriangleCalculator(3, 4, 5)
        self.assertEqual(calc.get_area(), 6.0)
        # проверка площади треугольника с допустимыми сторонами

    def test_equilateral_on_lower_bound(self):
        calc = TriangleCalculator(1, 1, 1)
        # площадь округляем до сотых 0,43
        self.assertAlmostEqual(calc.get_area(), 0.43, places=2)
        # минимальное значение стороны

    def test_permutation_same_result(self):
        calc = TriangleCalculator(5, 4, 3)
        self.assertEqual(calc.get_area(), 6.0)
        # перестановка сторон треугольника


class TestNegativeTriangle(unittest.TestCase):
        # негативные тесты

    def test_side_below_min(self):
        with self.assertRaises(SideException) as ctx:
            TriangleCalculator(0.99, 1, 1)
        self.assertIn("Стороны должны быть от 1 до 100", str(ctx.exception))
        # cторона < 1

    def test_side_at_max_boundary(self):
        with self.assertRaises(SideException) as ctx:
            TriangleCalculator(100, 50, 50)
        self.assertIn("Стороны должны быть от 1 до 100", str(ctx.exception))
        # cторона >= 100

    def test_non_existent_triangle(self):
        with self.assertRaises(SideException) as ctx:
            TriangleCalculator(1, 1, 2.5)
        self.assertIn("Недопустимые длины сторон", str(ctx.exception))
        # несуществующий треугольник


if __name__ == "__main__":
    unittest.main()
