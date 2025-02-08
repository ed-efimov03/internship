from abc import ABC, abstractmethod

def validate_soldier(func):
    def wrapper(self):
        if not isinstance(self, Soldier):
            raise TypeError("Объект не является экземпляром Soldier")
        return func(self)
    return wrapper

class Soldier(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Infantry(Soldier):
    @validate_soldier
    def move(self):
        print("Пехота передвигается в пешем порядке")

    @validate_soldier
    def attack(self):
        print("Пехота участвует в ближнем бою")

    @validate_soldier
    def defend(self):
        print("Пехота держит строй")

class Cavalry(Soldier):
    @validate_soldier
    def move(self):
        print("Кавалерия передвигается верхом")

    @validate_soldier
    def attack(self):
        print("Кавалерия переходит в атаку")

    @validate_soldier
    def defend(self):
        print("Кавалерия защищает фланги")

class Army:
    def __init__(self):
        self.list_soldiers = list()

    def add_soldier(self, soldier):
        self.list_soldiers.append(soldier)

    def attack(self):
        for soldier in self.list_soldiers:
            soldier.move()
            soldier.attack()

    def defend(self):
        for soldier in self.list_soldiers:
            soldier.move()
            soldier.defend()

army = Army()
army.add_soldier(Infantry())
army.add_soldier(Cavalry())
army.add_soldier(Infantry())
army.add_soldier(Cavalry())

army.attack()
army.defend()