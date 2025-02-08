from abc import ABC, abstractmethod

class Ingredient(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return f"{self.quantity} кг"
    
class Fruit(Ingredient):
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return f"{self.quantity} кг"
    
carrot = Vegetable("Морковь", 5)
apple = Fruit("Яблоки", 10)

print(carrot.get_name())
print(carrot.get_quantity())

print(apple.get_name())
print(apple.get_quantity())