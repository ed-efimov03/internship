RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант", "прапорщик", "старший прапорщик"]

def print_info(class_to_decorate):
    """Декоратор, который выводит информацию о созданном персонаже.
    
    Этот декоратор выводит информацию о типе создаваемого персонажа и его атрибутах.

    Args:
        class_to_decorate (type): Класс, который будет декорирован.
    
    Returns:
        class: Декорированный класс.
    """
    class DecoratedClass(class_to_decorate):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"Создан новый игровой персонаж типа {class_to_decorate.__name__} с атрибутами: {self.__dict__}")
    return DecoratedClass

@print_info
class Soldier:
    """Класс, представляющий солдата.

    Этот класс хранит информацию о солдате, таком как его звание и служебный номер.
    Также предоставляет методы для повышения и понижения звания.

    Attributes:
        name (str): Имя солдата.
        __rank (str): Звание солдата (закрытый атрибут).
        __service_number (int): Служебный номер солдата (закрытый атрибут).
    """

    def __init__(self, name: str, rank: str, service_number: int):
        """Инициализирует экземпляр класса Soldier.

        Args:
            name (str): Имя солдата.
            rank (str): Звание солдата.
            service_number (int): Служебный номер солдата.
        """

        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self) -> str:
        """Возвращает звание солдата.

        Returns:
            str: Звание солдата.
        """
        print(f"Персонаж {self.name} имеет звание {self.__rank}")

        return self.__rank
    
    def get_service_number(self):
        """Возвращает служебный номер солдата.

        Returns:
            int: Служебный номер солдата.
        """

        return self.__service_number
    
    def promote(self):
        """Повышает звание солдата, если это возможно.
        
        Солдат может быть повышен в звании, если его звание не является самым высоким.
        """

        if self.__rank in RANKS[:-1]:
            self.__rank = RANKS[RANKS.index(self.__rank) + 1]
            print(f"{self.name} повышен в звании, он теперь {self.__rank}")
    
    def demote(self):
        """Понижает звание солдата, если это возможно.

        Солдат может быть понижен в звании, если его звание не является самым низким.
        """
        
        if self.__rank in RANKS[1:]:
            self.__rank = RANKS[RANKS.index(self.__rank) - 1]
            print(f"{self.name} понижен в звании, он теперь {self.__rank}")

# Пример использования
soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")

soldier1.get_rank()
soldier1.promote()    
soldier1.demote()     
