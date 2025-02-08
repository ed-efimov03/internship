RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант", "прапорщик", "старший прапорщик"]

def print_info(class_to_decorate):
    class DecoratedCalss(class_to_decorate):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"Создан новый игровой персонаж типа {class_to_decorate.__name__} с атрибутами: {self.__dict__}")
    return DecoratedCalss

@print_info
class Soldier:
    def __init__(self, name: str, rank: str, service_number: int):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        print(f"Персонаж {self.name} имеет звание {self.__rank}")
        return self.__rank
    
    def get_service_number(self):
        return self.__service_number
    
    def promote(self):
        if self.__rank in RANKS[:-1]:
            self.__rank = RANKS[RANKS.index(self.__rank) + 1]
            print(f"{self.name} повышен в звании, он теперь {self.__rank}")
    
    def demote(self):
        if self.__rank in RANKS[1:]:
            self.__rank = RANKS[RANKS.index(self.__rank) - 1]
            print(f"{self.name} понижен в звании, он теперь {self.__rank}")

soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")

soldier1.get_rank()  

soldier1.promote()   

soldier1.demote()