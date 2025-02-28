import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class IsoscelesTrapezoid:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def distance(self, a, b):
        return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

    def cross_product(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

    def is_isosceles(self):
        cross_product1 = self.cross_product(self.p1, self.p2, self.p4)
        cross_product2 = self.cross_product(self.p3, self.p4, self.p2)

        bases_parallel = abs(cross_product1) < 1e-6 and abs(cross_product2) < 1e-6

        leg1_length = self.distance(self.p1, self.p4)
        leg2_length = self.distance(self.p2, self.p3)

        legs_equal = abs(leg1_length - leg2_length) < 1e-6

        return bases_parallel and legs_equal

    @property
    def side1_length(self):
        return self.distance(self.p1, self.p2)

    @property
    def side2_length(self):
        return self.distance(self.p2, self.p3)

    @property
    def side3_length(self):
        return self.distance(self.p3, self.p4)

    @property
    def side4_length(self):
        return self.distance(self.p4, self.p1)

    @property
    def perimeter(self):
        return self.side1_length + self.side2_length + self.side3_length + self.side4_length

    @property
    def area(self):
        h = abs(self.p1.y - self.p4.y)
        return ((self.side1_length + self.side3_length) / 2) * h

    def print_details(self):
        print(f"Длина первой стороны: {self.side1_length}")
        print(f"Длина второй стороны: {self.side2_length}")
        print(f"Длина третьей стороны: {self.side3_length}")
        print(f"Длина 4 стороны: {self.side4_length}")
        print(f"Периметр: {self.perimeter}")
        print(f"Область: {self.area}")


# Пример использования
p1 = Point(4, 4)
p2 = Point(5, 4)
p3 = Point(5, 4)
p4 = Point(4, 4)

trapezoid = IsoscelesTrapezoid(p1, p2, p3, p4)

print(f"Равнобедренная?: {trapezoid.is_isosceles()}")

if trapezoid.is_isosceles():
    trapezoid.print_details()