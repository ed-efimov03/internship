from abc import ABC, abstractmethod

class Starship(ABC):
    """Абстрактный класс, представляющий космический корабль.

    Этот класс служит базой для всех типов космических кораблей, определяя обязательные методы для их работы.

    Методы:
        warp_speed: Включить варп-двигатели для путешествия на сверхсветовых скоростях.
        fire_weapon: Орудие на борту корабля должно быть готово к атаке.
        self_destruct: Активировать систему самоуничтожения корабля.
    """

    @abstractmethod
    def warp_speed(self):
        """Включить варп-двигатели для путешествия на сверхсветовых скоростях."""
        pass
    
    @abstractmethod
    def fire_weapon(self):
        """Активировать оружие на борту для атаки."""
        pass

    @abstractmethod
    def self_destruct(self):
        """Активировать систему самоуничтожения корабля."""
        pass

class FederationStarship(Starship):
    """Класс, представляющий корабль Федерации.

    Этот класс реализует методы для работы с варп-двигателями, оружием и системой самоуничтожения.

    Методы:
        warp_speed: Включить варп-двигатели Федерации.
        fire_weapon: Использовать фотонные торпеды как оружие.
        self_destruct: Запустить систему самоуничтожения Федерации.
    """
    
    def warp_speed(self):
        """Включить варп-двигатели Федерации."""
        if not isinstance(self, FederationStarship):
            raise ValueError("Ошибка: Корабль должен быть типа FederationStarship.")
        print("Включить варп-двигатели!")
    
    def fire_weapon(self):
        """Использовать фотонные торпеды."""
        if not isinstance(self, FederationStarship):
            raise ValueError("Ошибка: Корабль должен быть типа FederationStarship.")
        print("Выпустить фотонные торпеды!")

    def self_destruct(self):
        """Запустить систему самоуничтожения Федерации."""
        if not isinstance(self, FederationStarship):
            raise ValueError("Ошибка: Корабль должен быть типа FederationStarship.")
        print("Запускаю систему самоуничтожения...")

class KlingonWarship(Starship):
    """Класс, представляющий военный корабль клингонов.

    Этот класс реализует методы для работы с маскировочным устройством, фазерами и системой самоуничтожения.

    Методы:
        warp_speed: Включить маскировочное устройство клингонов.
        fire_weapon: Использовать фазеры как оружие.
        self_destruct: Запустить протокол самоуничтожения клингонов.
    """
    
    def warp_speed(self):
        """Включить маскировочное устройство клингонов."""
        if not isinstance(self, KlingonWarship):
            raise ValueError("Ошибка: Корабль должен быть типа KlingonWarship.")
        print("Включить маскировочное устройство!")
    
    def fire_weapon(self):
        """Использовать фазеры как оружие."""
        if not isinstance(self, KlingonWarship):
            raise ValueError("Ошибка: Корабль должен быть типа KlingonWarship.")
        print("Стрелять из фазеров!")

    def self_destruct(self):
        """Запустить протокол самоуничтожения клингонов."""
        if not isinstance(self, KlingonWarship):
            raise ValueError("Ошибка: Корабль должен быть типа KlingonWarship.")
        print("Запускаю протокол самоуничтожения...")


# Пример использования
enterprise = FederationStarship()
bird_of_prey = KlingonWarship()

enterprise.warp_speed()
bird_of_prey.warp_speed()

enterprise.fire_weapon()
bird_of_prey.fire_weapon()

enterprise.self_destruct()
bird_of_prey.self_destruct()
