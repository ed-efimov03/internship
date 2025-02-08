# Импортируем необходимые модули: ABC (Abstract Base Class) и abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Создаем декоратор validate_soldier для проверки, что объект является экземпляром класса Soldier
def validate_soldier(func):
    # Внутренняя функция-обертка, которая выполняет проверку
    def wrapper(self):
        if not isinstance(self, Soldier):  # Проверяем, является ли объект экземпляром Soldier
            raise TypeError("Объект не является экземпляром Soldier")  # Если нет, выбрасываем исключение
        return func(self)  # Если проверка пройдена, вызываем исходный метод
    return wrapper  # Возвращаем функцию-обертку

# Создаем абстрактный класс Soldier, который будет базовым классом для всех типов солдат
class Soldier(ABC):
    # Абстрактный метод для передвижения
    @abstractmethod
    def move(self):
        pass

    # Абстрактный метод для атаки
    @abstractmethod
    def attack(self):
        pass

    # Абстрактный метод для защиты
    @abstractmethod
    def defend(self):
        pass

# Создаем класс Infantry (пехота), который наследует абстрактный класс Soldier
class Infantry(Soldier):
    # Реализация метода move для пехоты с использованием декоратора validate_soldier
    @validate_soldier
    def move(self):
        print("Пехота передвигается в пешем порядке")

    # Реализация метода attack для пехоты с использованием декоратора validate_soldier
    @validate_soldier
    def attack(self):
        print("Пехота участвует в ближнем бою")

    # Реализация метода defend для пехоты с использованием декоратора validate_soldier
    @validate_soldier
    def defend(self):
        print("Пехота держит строй")

# Создаем класс Cavalry (кавалерия), который также наследует абстрактный класс Soldier
class Cavalry(Soldier):
    # Реализация метода move для кавалерии с использованием декоратора validate_soldier
    @validate_soldier
    def move(self):
        print("Кавалерия передвигается верхом")

    # Реализация метода attack для кавалерии с использованием декоратора validate_soldier
    @validate_soldier
    def attack(self):
        print("Кавалерия переходит в атаку")

    # Реализация метода defend для кавалерии с использованием декоратора validate_soldier
    @validate_soldier
    def defend(self):
        print("Кавалерия защищает фланги")

# Создаем класс Army (армия), который управляет группой солдат
class Army:
    def __init__(self):
        self.list_soldiers = list()  # Инициализация списка солдат

    # Метод для добавления солдата в армию
    def add_soldier(self, soldier):
        self.list_soldiers.append(soldier)  # Добавляем солдата в список

    # Метод для выполнения атаки всеми солдатами в армии
    def attack(self):
        for soldier in self.list_soldiers:  # Проходим по каждому солдату
            soldier.move()  # Вызываем метод move
            soldier.attack()  # Вызываем метод attack

    # Метод для выполнения защиты всеми солдатами в армии
    def defend(self):
        for soldier in self.list_soldiers:  # Проходим по каждому солдату
            soldier.move()  # Вызываем метод move
            soldier.defend()  # Вызываем метод defend

# Создаем экземпляр армии
army = Army()
# Добавляем пехотинцев и кавалеристов в армию
army.add_soldier(Infantry())
army.add_soldier(Cavalry())
army.add_soldier(Infantry())
army.add_soldier(Cavalry())

# Выполняем атаку армии
army.attack()
# Выполняем защиту армии
army.defend()