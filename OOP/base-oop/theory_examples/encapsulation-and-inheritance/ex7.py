class Animal:
    """Класс, представляющий животное.

    Этот класс хранит информацию о животном.
    Также предоставляет методы для имитации его поведения.

    Attributes:
        name (str): Кличка животного
        species (str): Вид животного
        legs (int): Кол-во ног
    """

    def __init__(self, name: str, species: str, legs: int):
        """Инициализирует экземляр класса Animal.

        Args:
            name (str): Кличка животного
            species (str): Вид животного
            legs (int): Кол-во ног

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and isinstance(species, str) and isinstance(legs, int)):
            raise ValueError("Вы ввели невалидные значения")

        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        """Имитирует процесс додачи голоса.
        """

        print(f"{self.name} подает голос")

    def move(self):
        """Имитирует процесс дергания хвостом.
        """

        print(f"{self.name} дергает хвостом")

class Dog(Animal):
    """Класс, представляющий собаку.

    Наследуется от Animal и добавляет информацию о породе.

    Attributes:
        name (str): Кличка собаки
        breed (str): Порода собаки
        legs (int): Кол-во ног собаки
    """

    def __init__(self, name: str, breed: str, legs: int):
        """Инициализирует экземляр класса Dog.

        Args:
            name (str): Кличка собаки
            breed (str): Порода собаки
            legs (int): Кол-во ног собаки

        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and isinstance(breed, str) and isinstance(legs, int)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, breed, legs)
        self.breed = breed
    
    def bark(self):
        """Имитирует процесс лаиния.
        """

        print(f"{self.breed} {self.name} лает")

class Bird(Animal):
    """Класс, представляющий птицу.

    Наследуется от Animal и добавляет информацию о размахе крыльев.

    Attributes:
        name (str): Кличка птицы
        species (str): Вид птицы
        wingspan (int): Размах крыльев птицы
    """

    def __init__(self, name: str, species: str, wingspan: int):
        """Инициализирует экземляр класса Dog.

        Args:
            name (str): Кличка птицы
            species (str): Вид птицы
            wingspan (int): Размах крыльев птицы
        
        Raises:
            ValueError: Невалидное значение
        """

        if not(isinstance(name, str) and isinstance(species, str) and isinstance(wingspan, int)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, species, 2)
        self.wingspan = wingspan
    
    def fly(self):
        """Имитирует процесс полета.
        """

        print(f"{self.species} {self.name} летaeт")


#Проверяем работу программы
dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)

dog.voice()
bird.voice()
dog.move()
bird.move()

dog.bark()
bird.fly()