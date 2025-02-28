from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self, delta_x, delta_y):
        pass


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self):
        print(f"Квадрат рисуется с ({self.x}, {self.y}) со стороной {self.side_length}")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Круг рисуется с ({self.x}, {self.y}) и радиусом {self.radius}")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


# Пример использования
square = Square(15, 11, 6)
square.draw()
square.move(2, 7)
square.draw()