#Импортируем модуль math для математических вычислений
import math

class Shape:
    """Базовый класс для геометрических фигур.

    Attributes:
        color (str): Цвет
    """

    def __init__(self, color: str):
        """Инициализирует экземляр класса Shape.

        Args:
            color (str): Цвет

        Raises:
            ValueError: Невалидное значение.
        """

        if not isinstance(color, str):
            raise ValueError("Вы ввели невалидные значения")
        
        self.color = color

    def describe(self):
        print(f"Это геометрическая фигура, цвет - {self.color}.")

class Circle(Shape):
    """Класс Circle (Круг), наследуется от Shape.

    Attributes:
        color (str): Цвет
        radius (float): Радиус
    """

    def __init__(self, color: str, radius: float):
        """Инициализирует экземляр класса Circle.
        Args:
            color (str): Цвет
            radius (float): Радиус

        Raises:
            ValueError: Невалидное значение.
        """

        if not (isinstance(color, str) and (isinstance(radius, int) or isinstance(radius, float))):
            raise ValueError("Вы ввели невалидные значения")
        
        super().__init__(color)
        self.radius = radius
    
    def area(self) -> float:
        """Возращает площадь круга

        Returns:
            float: Площадь круга
        """

        return round(math.pi * self.radius * self.radius, 2)

    def describe(self):
        """Выводит описание круга
        """

        super().describe()
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")

class Rectangle(Shape):
    """Класс Rectangle (Прямоугольник), наследуется от Shape.

    Attributes:
        color (str): Цвет
        length (float): Длина
        width (float): Ширина
    """

    def __init__(self, color: str, length: float, width: float):
        """Инициализирует экземляр класса Rectangle.

        Args:
            color (str): Цвет
            length (float): Длина
            width (float): Ширина

        Raises:
            ValueError: Невалидное значение.
        """
        if not (isinstance(color, str) and (isinstance(length, int) or isinstance(length, float)) and 
                (isinstance(width, int) or isinstance(width, float))):
            raise ValueError("Вы ввели невалидные значения")
        
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Возращает площадь прямоугольника

        Returns:
            float: Площадь прямоугольника
        """

        return round(self.length * self.width, 2)
    
    def describe(self):
        """Выводит описание прямоугольника.
        """
        
        super().describe()
        print(f"Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см.")

class Triangle(Shape):
    """Класс Triangle (Треугольник), наследуется от Shape.

    Attributes:
        color (str): Цвет
        base (float): Основание
        height (float): Высота
    """

    def __init__(self, color: str, base: float, height: float):
        """Инициализирует экземляр класса Triangle.

        Args:
            color (str): Цвет
            base (float): Основание
            height (float): Высота

        Raises:
            ValueError: Невалидное значение.
        """
        if not (isinstance(color, str) and (isinstance(base, int) or isinstance(base, float)) and 
                (isinstance(height, int) or isinstance(height, float))):
            raise ValueError("Вы ввели невалидные значения")
        
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self) -> float:
        """Возращает площадь треугольника.

        Returns:
            float: Площадь треугольника
        """

        return round(0.5 * self.base * self.height, 2)
    
    def describe(self):
        """Выводит описание треугольника.
        """

        super().describe()
        print(f"Это {self.color} треугольник с основанием {self.base} см и высотой {self.height} см.")


#Проверяем работу программы
circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()

print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")