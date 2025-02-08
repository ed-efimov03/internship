# Декоратор для отображения информации о тестировании производительности
def show_info(old_func):
    def wrapper(*args, **kwargs):
        print("Начинаем тест производительности...")  # Сообщение перед выполнением функции
        result = old_func(*args, **kwargs)  # Выполнение оригинальной функции
        print("Тест производительности завершен.")  # Сообщение после выполнения функции
        return result  # Возвращаем результат оригинальной функции (если есть)
    return wrapper

# Базовый класс для компьютеров
class Computer:
    def __init__(self, model: str, processor: str, memory: str):
        self.model = model  # Название модели
        self.processor = processor  # Процессор
        self.memory = memory  # Объем оперативной памяти

# Класс настольного компьютера, наследуется от Computer
class Desktop(Computer):
    @show_info  # Применяем декоратор к методу run
    def run(self):
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

# Класс ноутбука, наследуется от Computer
class Laptop(Computer):
    @show_info  # Применяем декоратор к методу run
    def run(self):
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

# Класс магазина компьютеров
class ComputerStore:
    def __init__(self):
        self.computers_list = []  # Список компьютеров в магазине

    # Метод добавления компьютера в магазин
    def add_computer(self, computer: Computer):
        self.computers_list.append(computer)

    # Метод для запуска тестов на всех компьютерах
    def run_tests(self):
        for comp in self.computers_list:
            comp.run()

# Создание магазина и добавление компьютеров
store = ComputerStore()
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб"))  # Настольный ПК
store.add_computer(Laptop("Dell Xtra", "Intel Core i5-13600K", "32 Гб"))  # Ноутбук
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))  # Настольный ПК

# Запуск тестов производительности
store.run_tests()
