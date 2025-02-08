# Импортируем необходимые модули: ABC (Abstract Base Class) и abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Создаем абстрактный класс Ingredient, который будет базовым классом для всех ингредиентов
class Ingredient(ABC):
    # Абстрактный метод для получения названия ингредиента
    @abstractmethod
    def get_name(self):
        pass

    # Абстрактный метод для получения количества ингредиента
    @abstractmethod
    def get_quantity(self):
        pass

# Создаем класс Vegetable, который наследует абстрактный класс Ingredient
class Vegetable(Ingredient):
    # Конструктор класса, принимающий название и количество овоща
    def __init__(self, name: str, quantity: int):
        self.name = name  # Инициализация названия овоща
        self.quantity = quantity  # Инициализация количества овоща

    # Реализация метода get_name для овоща
    def get_name(self):
        return self.name  # Возвращает название овоща
    
    # Реализация метода get_quantity для овоща
    def get_quantity(self):
        return f"{self.quantity} кг"  # Возвращает количество овоща в формате строки
    
# Создаем класс Fruit, который также наследует абстрактный класс Ingredient
class Fruit(Ingredient):
    # Конструктор класса, принимающий название и количество фрукта
    def __init__(self, name: str, quantity: int):
        self.name = name  # Инициализация названия фрукта
        self.quantity = quantity  # Инициализация количества фрукта

    # Реализация метода get_name для фрукта
    def get_name(self):
        return self.name  # Возвращает название фрукта
    
    # Реализация метода get_quantity для фрукта
    def get_quantity(self):
        return f"{self.quantity} кг"  # Возвращает количество фрукта в формате строки
    
# Создаем экземпляр класса Vegetable с названием "Морковь" и количеством 5 кг
carrot = Vegetable("Морковь", 5)
# Создаем экземпляр класса Fruit с названием "Яблоки" и количеством 10 кг
apple = Fruit("Яблоки", 10)

# Выводим название моркови
print(carrot.get_name())
# Выводим количество моркови
print(carrot.get_quantity())

# Выводим название яблок
print(apple.get_name())
# Выводим количество яблок
print(apple.get_quantity())