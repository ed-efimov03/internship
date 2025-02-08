import math

class Shape:
    def __init__(self, color: str):
        self.color = color

    def describe(self):
        print(f"Это геометрическая фигура, цвет - {self.color}.")

class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius * self.radius, 2)

    def describe(self):
        super().describe()
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")

class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return round(self.length * self.width, 2)
    
    def describe(self):
        super().describe()
        print(f"Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см.")

class Triangle(Shape):
    def __init__(self, color: str, base: float, height: float):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        return round(0.5 * self.base * self.height, 2)
    
    def describe(self):
        super().describe()
        print(f"Это {self.color} треугольник с основанием {self.base} см и высотой {self.height} см.")
    
circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()

print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")