# Импортируем необходимые модули: ABC (Abstract Base Class) и abstractmethod для создания абстрактных классов и методов
from abc import ABC, abstractmethod

# Создаем абстрактный класс Starship, который будет базовым классом для всех типов звездолетов
class Starship(ABC):
    # Абстрактный метод для включения варп-скорости
    @abstractmethod
    def warp_speed(self):
        pass
    
    # Абстрактный метод для стрельбы из оружия
    @abstractmethod
    def fire_weapon(self):
        pass

    # Абстрактный метод для самоуничтожения звездолета
    @abstractmethod
    def self_destruct(self):
        pass

# Создаем класс FederationStarship, который наследует абстрактный класс Starship
class FederationStarship(Starship):
    # Реализация метода warp_speed для звездолета Федерации
    def warp_speed(self):
        print("Включить варп-двигатели!")
    
    # Реализация метода fire_weapon для звездолета Федерации
    def fire_weapon(self):
        print("Выпустить фотонные торпеды!")

    # Реализация метода self_destruct для звездолета Федерации
    def self_destruct(self):
        print("Запускаю систему самоуничтожения...")

# Создаем класс KlingonWarship, который также наследует абстрактный класс Starship
class KlingonWarship(Starship):
    # Реализация метода warp_speed для клингонского боевого корабля
    def warp_speed(self):
        print("Включить маскировочное устройство!")
    
    # Реализация метода fire_weapon для клингонского боевого корабля
    def fire_weapon(self):
        print("Стрелять из фазеров!")

    # Реализация метода self_destruct для клингонского боевого корабля
    def self_destruct(self):
        print("Запускаю протокол самоуничтожения...")

# Создаем экземпляр звездолета Федерации
enterprise = FederationStarship()
# Создаем экземпляр клингонского боевого корабля
bird_of_prey = KlingonWarship()

# Вызываем метод warp_speed для звездолета Федерации
enterprise.warp_speed()
# Вызываем метод warp_speed для клингонского боевого корабля
bird_of_prey.warp_speed()

# Вызываем метод fire_weapon для звездолета Федерации
enterprise.fire_weapon()
# Вызываем метод fire_weapon для клингонского боевого корабля
bird_of_prey.fire_weapon()

# Вызываем метод self_destruct для звездолета Федерации
enterprise.self_destruct()
# Вызываем метод self_destruct для клингонского боевого корабля
bird_of_prey.self_destruct()