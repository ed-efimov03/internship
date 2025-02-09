def show_info(old_func):
    """Декоратор для тестирования производительности компьютеров."""
    def wrapper(*args, **kwargs):
        print("Начинаем тест производительности...")  
        result = old_func(*args, **kwargs) 
        print("Тест производительности завершен.")  
        return result  
    return wrapper


class Computer:
    """Базовый класс для всех типов компьютеров."""
    
    def __init__(self, model: str, processor: str, memory: str):
        """
        Инициализирует параметры компьютера.
        
        :param model: Модель компьютера
        :param processor: Процессор
        :param memory: Оперативная память
        """
        self.model = model  
        self.processor = processor  
        self.memory = memory  


class Desktop(Computer):
    """Класс для настольных компьютеров."""
    
    @show_info  
    def run(self):
        """Запуск настольного компьютера."""
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class Laptop(Computer):
    """Класс для ноутбуков."""
    
    @show_info 
    def run(self):
        """Запуск ноутбука."""
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class ComputerStore:
    """Класс для магазина компьютеров."""
    
    def __init__(self):
        """Инициализирует пустой список для хранения компьютеров."""
        self.computers_list = []  

    def add_computer(self, computer: Computer):
        """
        Добавляет компьютер в список магазина.
        
        :param computer: Экземпляр класса Computer
        """
        if isinstance(computer, Computer):
            self.computers_list.append(computer)
        else:
            raise ValueError("Добавляемый объект должен быть экземпляром класса Computer или его подклассов.")

    def run_tests(self):
        """Запускает тесты производительности для всех компьютеров в магазине."""
        for comp in self.computers_list:
            comp.run()


# Создание экземпляра магазина
store = ComputerStore()

# Добавление различных типов компьютеров
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб")) 
store.add_computer(Laptop("Dell Xtra", "Intel Core i5-13600K", "32 Гб"))  
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))  

# Запуск тестов производительности для всех компьютеров
store.run_tests()
