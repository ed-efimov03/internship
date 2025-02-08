class Animal:
    def __init__(self, name: str, species: str, legs: int):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f"{self.name} подает голос")

    def move(self):
        print(f"{self.name} дергает хвостом")

class Dog(Animal):
    def __init__(self, name: str, breed: str, legs: int):
        super().__init__(name, breed, legs)
        self.breed = breed
    
    def bark(self):
        print(f"{self.breed} {self.name} лает")

class Bird(Animal):
    def __init__(self, name: str, species: str, wingspan: float):
        super().__init__(name, species, 2)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.species} {self.name} летaeт")

dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)

dog.voice()
bird.voice()
dog.move()
bird.move()

dog.bark()
bird.fly()