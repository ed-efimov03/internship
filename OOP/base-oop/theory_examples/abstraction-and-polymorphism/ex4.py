from abc import ABC, abstractmethod

class Dinosaur(ABC):
    """Абстрактный класс для динозавра.

    Этот класс задает базовые методы для получения данных о динозавре: имя, вид, рост, вес и рацион.
    Все методы должны быть реализованы в дочерних классах.

    Методы:
        get_personal_name: Метод для получения имени динозавра.
        get_breed: Метод для получения вида динозавра.
        get_height: Метод для получения роста динозавра.
        get_weight: Метод для получения веса динозавра.
        get_diet: Метод для получения рациона динозавра.
    """

    @abstractmethod
    def get_personal_name(self):
        """Возвращает имя динозавра."""
        pass

    @abstractmethod
    def get_breed(self):
        """Возвращает вид динозавра."""
        pass

    @abstractmethod
    def get_height(self):
        """Возвращает рост динозавра."""
        pass

    @abstractmethod
    def get_weight(self):
        """Возвращает вес динозавра."""
        pass

    @abstractmethod
    def get_diet(self):
        """Возвращает рацион динозавра (плотоядный или травоядный)."""
        pass

class Carnivore(Dinosaur):
    """Класс для плотоядных динозавров.

    Этот класс наследует от Dinosaur и реализует методы для плотоядных динозавров.

    Атрибуты:
        breed (str): Вид динозавра.
        personal_name (str): Имя динозавра.
        weight (float): Вес динозавра в килограммах.
        height (float): Рост динозавра в сантиметрах.
    """

    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        """Инициализирует плотоядного динозавра с его видом, именем, весом и ростом."""
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        """Возвращает имя динозавра."""
        return self.personal_name

    def get_breed(self):
        """Возвращает вид динозавра."""
        return self.breed

    def get_height(self):
        """Возвращает рост динозавра."""
        return self.height

    def get_weight(self):
        """Возвращает вес динозавра."""
        return self.weight

    def get_diet(self):
        """Возвращает рацион динозавра: Плотоядный."""
        return "Плотоядный"

class Herbivore(Dinosaur):
    """Класс для травоядных динозавров.

    Этот класс наследует от Dinosaur и реализует методы для травоядных динозавров.

    Атрибуты:
        breed (str): Вид динозавра.
        personal_name (str): Имя динозавра.
        weight (float): Вес динозавра в килограммах.
        height (float): Рост динозавра в сантиметрах.
    """

    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        """Инициализирует травоядного динозавра с его видом, именем, весом и ростом."""
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        """Возвращает имя динозавра."""
        return self.personal_name

    def get_breed(self):
        """Возвращает вид динозавра."""
        return self.breed

    def get_height(self):
        """Возвращает рост динозавра."""
        return self.height

    def get_weight(self):
        """Возвращает вес динозавра."""
        return self.weight

    def get_diet(self):
        """Возвращает рацион динозавра: Травоядный."""
        return "Травоядный"

class DinosaurPark:
    """Класс, представляющий парк динозавров.

    Этот класс управляет списком динозавров, позволяя добавлять динозавров в парк и фильтровать их по типу рациона.

    Атрибуты:
        dinosaurs_list (list): Список динозавров в парке.
    
    Методы:
        add_dinosaur: Добавляет динозавра в парк.
        list_dinosaurs: Возвращает список всех динозавров в парке.
        list_carnivores: Возвращает список всех плотоядных динозавров.
        list_herbivores: Возвращает список всех травоядных динозавров.
    """

    def __init__(self):
        """Инициализирует парк динозавров с пустым списком."""
        self.dinosaurs_list = []

    def add_dinosaur(self, dinosaur: Dinosaur):
        """Добавляет динозавра в парк.

        Args:
            dinosaur (Dinosaur): Экземпляр динозавра для добавления.
        """
        self.dinosaurs_list.append(dinosaur)

    def list_dinosaurs(self):
        """Возвращает список всех динозавров в парке."""
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(),
                 dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet()) for dinosaur in self.dinosaurs_list]

    def list_carnivores(self):
        """Возвращает список всех плотоядных динозавров в парке."""
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(),
                 dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Carnivore)]

    def list_herbivores(self):
        """Возвращает список всех травоядных динозавров в парке."""
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(),
                 dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Herbivore)]


# Создание экземпляров динозавров
t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

# Создание парка динозавров и добавление динозавров
park = DinosaurPark()
park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

# Вывод информации о динозаврах в парке
for dinosaur in park.list_dinosaurs():
    print(f'Имя: {dinosaur[0]}\n'
          f'Вид: {dinosaur[1]}\n'
          f'Рост: {dinosaur[2]} см\n'
          f'Вес: {dinosaur[3]} кг\n'
          f'Рацион: {dinosaur[4]}\n')
