# Список всех возможных званий в армии
RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант", "прапорщик", "старший прапорщик"]

# Декоратор, который добавляет функциональность для вывода информации при создании персонажа
def print_info(class_to_decorate):
    # Класс DecoratedCalss наследует класс class_to_decorate (например, Soldier)
    class DecoratedCalss(class_to_decorate):
        # Конструктор класса, который вызывает конструктор родительского класса и выводит информацию
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)  # Вызов конструктора родительского класса
            print(f"Создан новый игровой персонаж типа {class_to_decorate.__name__} с атрибутами: {self.__dict__}")
    return DecoratedCalss  # Возвращаем класс-обертку

# Применяем декоратор print_info к классу Soldier
@print_info
class Soldier:
    # Конструктор класса Soldier, инициализирует имя, звание и номер службы
    def __init__(self, name: str, rank: str, service_number: int):
        self.name = name  # Имя персонажа
        self.__rank = rank  # Звание персонажа (закрыто для прямого доступа)
        self.__service_number = service_number  # Номер службы персонажа

    # Метод для получения звания персонажа
    def get_rank(self):
        print(f"Персонаж {self.name} имеет звание {self.__rank}")
        return self.__rank  # Возвращаем звание
    
    # Метод для получения номера службы персонажа
    def get_service_number(self):
        return self.__service_number  # Возвращаем номер службы
    
    # Метод для повышения персонажа в звании
    def promote(self):
        # Если персонаж не имеет высшее звание, повышаем его
        if self.__rank in RANKS[:-1]:  # Проверка, что персонаж не на последнем ранге
            self.__rank = RANKS[RANKS.index(self.__rank) + 1]  # Устанавливаем следующее звание
            print(f"{self.name} повышен в звании, он теперь {self.__rank}")
    
    # Метод для понижения персонажа в звании
    def demote(self):
        # Если персонаж не имеет низшее звание, понижаем его
        if self.__rank in RANKS[1:]:  # Проверка, что персонаж не на первом ранге
            self.__rank = RANKS[RANKS.index(self.__rank) - 1]  # Устанавливаем предыдущее звание
            print(f"{self.name} понижен в звании, он теперь {self.__rank}")

# Создание нового объекта Soldier с именем, званием и номером службы
soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")

# Вызов метода для получения звания
soldier1.get_rank()  

# Повышение персонажа в звании
soldier1.promote()   

# Понижение персонажа в звании
soldier1.demote()   
