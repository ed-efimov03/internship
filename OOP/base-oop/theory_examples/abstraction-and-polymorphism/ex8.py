# Базовый класс для самолетов
class Aircraft:
    def __init__(self, model: str, manufacturer: str, capacity: int):
        self.model = model  # Модель самолета
        self.manufacturer = manufacturer  # Производитель
        self.capacity = capacity  # Вместимость (количество пассажиров или грузоподъемность)

# Класс пассажирского самолета, наследуется от Aircraft
class PassengerAircraft(Aircraft):
    def fly(self):
        print(f"Пассажирский самолет '{self.model}' вместимостью {self.capacity} человек, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с пассажирами на борту.")

# Класс грузового самолета, наследуется от Aircraft
class CargoAircraft(Aircraft):
    def fly(self):
        print(f"Грузовой самолет '{self.model}' грузоподъемностью {self.capacity} тонн, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с грузом на борту.")

# Класс аэропорта, содержащий список самолетов
class Airport:
    def __init__(self):
        self.aircrafts_list = []  # Список самолетов в аэропорту

    # Метод для добавления самолета в список
    def add_aircraft(self, aircraft: Aircraft):
        self.aircrafts_list.append(aircraft)

    # Метод для взлета всех самолетов
    def takeoff(self):
        for aircraft in self.aircrafts_list:
            aircraft.fly()

# Создание аэропорта и добавление самолетов
airport = Airport()
airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416))  # Пассажирский самолет
airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70))  # Грузовой самолет (70 тонн)
airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396))  # Пассажирский самолет

# Выполнение взлета всех самолетов
airport.takeoff()
