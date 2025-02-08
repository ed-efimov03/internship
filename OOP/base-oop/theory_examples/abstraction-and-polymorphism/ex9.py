def show_info(old_func):
    def wrapper(*args, **kwargs):
        print("Начинаем тест производительности...")  
        result = old_func(*args, **kwargs) 
        print("Тест производительности завершен.")  
        return result  
    return wrapper


class Computer:
    def __init__(self, model: str, processor: str, memory: str):
        self.model = model  
        self.processor = processor  
        self.memory = memory  


class Desktop(Computer):
    @show_info  
    def run(self):
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class Laptop(Computer):
    @show_info 
    def run(self):
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class ComputerStore:
    def __init__(self):
        self.computers_list = []  


    def add_computer(self, computer: Computer):
        self.computers_list.append(computer)


    def run_tests(self):
        for comp in self.computers_list:
            comp.run()


store = ComputerStore()
store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб")) 
store.add_computer(Laptop("Dell Xtra", "Intel Core i5-13600K", "32 Гб"))  
store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))  


store.run_tests()
