import math

class SideException(Exception):
    """Ошибка для недопустимых сторон"""
    pass

class TriangleCalculator:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        # спроверка диапазона сторон [1, 100)
        if not (1 <= self.a < 100 and 1 <= self.b < 100 and 1 <= self.c < 100):
            raise SideException("Стороны должны быть от 1 до 100")
        # проверка неравенства треугольника
        if (
                self.a >= self.b + self.c or
                self.b >= self.a + self.c or
                self.c >= self.a + self.b
        ):
            raise SideException("Недопустимые длины сторон")

    def get_area(self) -> float:
        # полупериметр
        p = (self.a + self.b + self.c) / 2
        # формула Герона
        try:
            area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        except ValueError:
            # если корень из отрицательного — пишем свою ошибку
            raise SideException("Невозможно вычислить площадь треугольника")
        return round(area, 2)

    def get_perimeter(self) -> float:
        # сумма сторон
        return self.a + self.b + self.c

    def get_type(self) -> str:
        # тип треугольника
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "scalene"