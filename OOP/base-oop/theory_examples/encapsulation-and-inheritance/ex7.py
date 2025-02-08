# Класс Animal представляет общее поведение для всех животных
class Animal:
    # Инициализация животного с именем, видом и количеством ног
    def __init__(self, name: str, species: str, legs: int):
        self.name = name  # Имя животного
        self.species = species  # Вид животного
        self.legs = legs  # Количество ног у животного

    # Метод для издания звука животным
    def voice(self):
        print(f"{self.name} подает голос")  # Животное издает звук

    # Метод для движения животного
    def move(self):
        print(f"{self.name} дергает хвостом")  # Животное двигается

# Класс Dog является наследником класса Animal и представляет поведение собаки
class Dog(Animal):
    # Инициализация собаки с именем, породой и количеством ног
    def __init__(self, name: str, breed: str, legs: int):
        super().__init__(name, breed, legs)  # Вызов конструктора родительского класса
        self.breed = breed  # Порода собаки
    
    # Метод для издания звука лающей собаки
    def bark(self):
        print(f"{self.breed} {self.name} лает")  # Собака лает

# Класс Bird является наследником класса Animal и представляет поведение птицы
class Bird(Animal):
    # Инициализация птицы с именем, видом и размахом крыльев
    def __init__(self, name: str, species: str, wingspan: float):
        super().__init__(name, species, 2)  # Вызов конструктора родительского класса, устанавливаем 2 ноги
        self.wingspan = wingspan  # Размах крыльев птицы
    
    # Метод для полета птицы
    def fly(self):
        print(f"{self.species} {self.name} летaeт")  # Птица летит

# Создаем объект собаки
dog = Dog("Геральт", "доберман", 4)
# Создаем объект птицы
bird = Bird("Вася", "попугай", 2)

# Вызываем методы для собаки
dog.voice()  # Собака подает голос
bird.voice()  # Птица подает голос
dog.move()  # Собака двигается
bird.move()  # Птица двигается

# Вызываем уникальные методы для собаки и птицы
dog.bark()  # Собака лает
bird.fly()  # Птица летит
