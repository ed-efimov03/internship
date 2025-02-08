# Импортируем необходимые модули: ABC (Abstract Base Class) и abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Создаем абстрактный класс Dinosaur, который будет базовым классом для всех динозавров
class Dinosaur(ABC):
    # Абстрактный метод для получения имени динозавра
    @abstractmethod
    def get_personal_name(self):
        pass

    # Абстрактный метод для получения вида динозавра
    @abstractmethod
    def get_breed(self):
        pass

    # Абстрактный метод для получения роста динозавра
    @abstractmethod
    def get_height(self):
        pass

    # Абстрактный метод для получения веса динозавра
    @abstractmethod
    def get_weight(self):
        pass

    # Абстрактный метод для получения рациона динозавра
    @abstractmethod
    def get_diet(self):
        pass

# Создаем класс Carnivore (хищник), который наследует абстрактный класс Dinosaur
class Carnivore(Dinosaur):
    # Конструктор класса, принимающий вид, имя, вес и рост динозавра
    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        self.breed = breed  # Инициализация вида динозавра
        self.personal_name = personal_name  # Инициализация имени динозавра
        self.weight = weight  # Инициализация веса динозавра
        self.height = height  # Инициализация роста динозавра

    # Реализация метода get_personal_name для хищника
    def get_personal_name(self):
        return self.personal_name  # Возвращает имя динозавра

    # Реализация метода get_breed для хищника
    def get_breed(self):
        return self.breed  # Возвращает вид динозавра

    # Реализация метода get_height для хищника
    def get_height(self):
        return self.height  # Возвращает рост динозавра

    # Реализация метода get_weight для хищника
    def get_weight(self):
        return self.weight  # Возвращает вес динозавра

    # Реализация метода get_diet для хищника
    def get_diet(self):
        return "Плотоядный"  # Возвращает рацион динозавра
    
# Создаем класс Herbivore (травоядный), который также наследует абстрактный класс Dinosaur
class Herbivore(Dinosaur):
    # Конструктор класса, принимающий вид, имя, вес и рост динозавра
    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        self.breed = breed  # Инициализация вида динозавра
        self.personal_name = personal_name  # Инициализация имени динозавра
        self.weight = weight  # Инициализация веса динозавра
        self.height = height  # Инициализация роста динозавра

    # Реализация метода get_personal_name для травоядного
    def get_personal_name(self):
        return self.personal_name  # Возвращает имя динозавра

    # Реализация метода get_breed для травоядного
    def get_breed(self):
        return self.breed  # Возвращает вид динозавра

    # Реализация метода get_height для травоядного
    def get_height(self):
        return self.height  # Возвращает рост динозавра

    # Реализация метода get_weight для травоядного
    def get_weight(self):
        return self.weight  # Возвращает вес динозавра

    # Реализация метода get_diet для травоядного
    def get_diet(self):
        return "Травоядный"  # Возвращает рацион динозавра
    
# Создаем класс DinosaurPark (парк динозавров), который управляет коллекцией динозавров
class DinosaurPark:
    def __init__(self):
        self.dinosaurs_list = []  # Инициализация списка динозавров

    # Метод для добавления динозавра в парк
    def add_dinosaur(self, dinosaur: Dinosaur):
        self.dinosaurs_list.append(dinosaur)  # Добавляем динозавра в список

    # Метод для получения списка всех динозавров в парке
    def list_dinosaurs(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list]

    # Метод для получения списка всех хищников в парке
    def list_carnivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Carnivore)]
    
    # Метод для получения списка всех травоядных в парке
    def list_herbivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Herbivore)]


# Создаем экземпляры динозавров
t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

# Создаем экземпляр парка динозавров
park = DinosaurPark()

# Добавляем динозавров в парк
park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

# Выводим информацию о всех динозаврах в парке
for dinosaur in park.list_dinosaurs():
    print(f'Имя: {dinosaur[0]}\n'
    f'Вид: {dinosaur[1]}\n'
    f'Вес: {dinosaur[2]} кг\n'
    f'Рост: {dinosaur[3]} см\n'
    f'Рацион: {dinosaur[4]}\n')