from abc import ABC, abstractmethod

def validate_soldier(func):
    """Декоратор для проверки типа объекта.

    Этот декоратор проверяет, является ли объект экземпляром класса Soldier перед выполнением метода.

    Args:
        func: Метод, который должен быть защищен от вызова на объектах других типов.

    Returns:
        Wrapper-функция, которая выполняет проверку типа объекта перед вызовом оригинального метода.
    """
    def wrapper(self):
        if not isinstance(self, Soldier):
            raise TypeError("Объект не является экземпляром Soldier")
        return func(self)
    return wrapper

class Soldier(ABC):
    """Абстрактный класс, представляющий солдата.

    Этот класс является базовым для всех типов солдат. Он задает методы для движения, атаки и защиты, которые должны быть реализованы в дочерних классах.

    Методы:
        move: Метод для движения солдата.
        attack: Метод для атаки солдата.
        defend: Метод для защиты солдата.
    """
    
    @abstractmethod
    def move(self):
        """Метод для движения солдата."""
        pass

    @abstractmethod
    def attack(self):
        """Метод для атаки солдата."""
        pass

    @abstractmethod
    def defend(self):
        """Метод для защиты солдата."""
        pass

class Infantry(Soldier):
    """Класс, представляющий пехоту.

    Этот класс наследует от Soldier и реализует конкретные действия для пехоты: движение, атаку и защиту.

    Методы:
        move: Пехота передвигается в пешем порядке.
        attack: Пехота участвует в ближнем бою.
        defend: Пехота держит строй.
    """

    @validate_soldier
    def move(self):
        """Пехота передвигается в пешем порядке."""
        print("Пехота передвигается в пешем порядке")

    @validate_soldier
    def attack(self):
        """Пехота участвует в ближнем бою."""
        print("Пехота участвует в ближнем бою")

    @validate_soldier
    def defend(self):
        """Пехота держит строй."""
        print("Пехота держит строй")

class Cavalry(Soldier):
    """Класс, представляющий кавалерию.

    Этот класс наследует от Soldier и реализует конкретные действия для кавалерии: движение, атаку и защиту.

    Методы:
        move: Кавалерия передвигается верхом.
        attack: Кавалерия переходит в атаку.
        defend: Кавалерия защищает фланги.
    """

    @validate_soldier
    def move(self):
        """Кавалерия передвигается верхом."""
        print("Кавалерия передвигается верхом")

    @validate_soldier
    def attack(self):
        """Кавалерия переходит в атаку."""
        print("Кавалерия переходит в атаку")

    @validate_soldier
    def defend(self):
        """Кавалерия защищает фланги."""
        print("Кавалерия защищает фланги")

class Army:
    """Класс, представляющий армию.

    Этот класс управляет списком солдат, позволяя добавлять солдат в армию и выполнять атаки и защиту.

    Атрибуты:
        list_soldiers (list): Список солдат в армии.

    Методы:
        add_soldier: Добавляет солдата в армию.
        attack: Выполняет атаку всеми солдатами в армии.
        defend: Выполняет защиту всеми солдатами в армии.
    """
    
    def __init__(self):
        """Инициализирует армию с пустым списком солдат."""
        self.list_soldiers = list()

    def add_soldier(self, soldier):
        """Добавляет солдата в армию.

        Args:
            soldier (Soldier): Солдат, который будет добавлен в армию.
        """
        self.list_soldiers.append(soldier)

    def attack(self):
        """Выполняет атаку всеми солдатами в армии."""
        for soldier in self.list_soldiers:
            soldier.move()
            soldier.attack()

    def defend(self):
        """Выполняет защиту всеми солдатами в армии."""
        for soldier in self.list_soldiers:
            soldier.move()
            soldier.defend()

# Создаем армию и добавляем солдат
army = Army()
army.add_soldier(Infantry())
army.add_soldier(Cavalry())
army.add_soldier(Infantry())
army.add_soldier(Cavalry())

# Выполняем атаку и защиту
army.attack()
army.defend()
