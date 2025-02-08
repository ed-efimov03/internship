from abc import ABC, abstractmethod

class Dinosaur(ABC):
    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

class Carnivore(Dinosaur):
    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Плотоядный"
    
class Herbivore(Dinosaur):
    def __init__(self, breed: str, personal_name: str, weight: float, height: float):
        self.breed = breed
        self.personal_name = personal_name
        self.weight = weight
        self.height = height

    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Травоядный"
    
class DinosaurPark:
    def __init__(self):
        self.dinosaurs_list = []

    def add_dinosaur(self, dinosaur: Dinosaur):
        self.dinosaurs_list.append(dinosaur)

    def list_dinosaurs(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list]

    def list_carnivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Carnivore)]
    
    def list_herbivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), 
               dinosaur.get_height(), dinosaur.get_weight(),
               dinosaur.get_diet()) for dinosaur in self.dinosaurs_list if isinstance(dinosaur, Herbivore)]

t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

park = DinosaurPark()

park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

for dinosaur in park.list_dinosaurs():
    print(f'Имя: {dinosaur[0]}\n'
    f'Вид: {dinosaur[1]}\n'
    f'Вес: {dinosaur[2]} кг\n'
    f'Рост: {dinosaur[3]} см\n'
    f'Рацион: {dinosaur[4]}\n')