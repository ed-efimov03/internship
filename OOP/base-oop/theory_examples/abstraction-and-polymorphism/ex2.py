from abc import ABC, abstractmethod

class Ingredient(ABC):
    """Абстрактный класс для ингредиента.

    Этот класс используется для создания общего интерфейса для всех типов ингредиентов, таких как овощи и фрукты.
    
    Методы:
        get_name: Возвращает имя ингредиента.
        get_quantity: Возвращает количество ингредиента.
    """

    @abstractmethod
    def get_name(self):
        """Возвращает имя ингредиента."""
        pass

    @abstractmethod
    def get_quantity(self):
        """Возвращает количество ингредиента."""
        pass

class Vegetable(Ingredient):
    """Класс, представляющий овощ.

    Этот класс наследует от Ingredient и представляет собой конкретный тип ингредиента - овощ.

    Атрибуты:
        name (str): Название овоща.
        quantity (int): Количество овоща в килограммах.

    Методы:
        get_name: Возвращает имя овоща.
        get_quantity: Возвращает количество овоща в килограммах.
    """

    def __init__(self, name: str, quantity: int):
        """Инициализирует объект овоща с заданными параметрами.

        Args:
            name (str): Название овоща.
            quantity (int): Количество овоща в килограммах.
        """
        self.name = name
        self.quantity = quantity

    def get_name(self):
        """Возвращает имя овоща."""
        return self.name
    
    def get_quantity(self):
        """Возвращает количество овоща в килограммах."""
        return f"{self.quantity} кг"
    
class Fruit(Ingredient):
    """Класс, представляющий фрукт.

    Этот класс наследует от Ingredient и представляет собой конкретный тип ингредиента - фрукт.

    Атрибуты:
        name (str): Название фрукта.
        quantity (int): Количество фрукта в килограммах.

    Методы:
        get_name: Возвращает имя фрукта.
        get_quantity: Возвращает количество фрукта в килограммах.
    """

    def __init__(self, name: str, quantity: int):
        """Инициализирует объект фрукта с заданными параметрами.

        Args:
            name (str): Название фрукта.
            quantity (int): Количество фрукта в килограммах.
        """
        self.name = name
        self.quantity = quantity

    def get_name(self):
        """Возвращает имя фрукта."""
        return self.name
    
    def get_quantity(self):
        """Возвращает количество фрукта в килограммах."""
        return f"{self.quantity} кг"
    
# Создаем объекты овощей и фруктов
carrot = Vegetable("Морковь", 5)
apple = Fruit("Яблоки", 10)

# Выводим информацию об ингредиентах
print(carrot.get_name())
print(carrot.get_quantity())

print(apple.get_name())
print(apple.get_quantity())
