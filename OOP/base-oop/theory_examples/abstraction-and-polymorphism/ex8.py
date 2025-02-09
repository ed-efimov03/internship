class Aircraft:
    """Класс, представляющий основной самолет."""
    
    def __init__(self, model: str, manufacturer: str, capacity: int):
        """
        Инициализирует параметры самолета.
        
        :param model: Модель самолета
        :param manufacturer: Производитель самолета
        :param capacity: Вместимость самолета (для пассажиров или груза)
        """
        self.model = model  
        self.manufacturer = manufacturer  
        self.capacity = capacity  


class PassengerAircraft(Aircraft):
    """Класс для пассажирских самолетов."""
    
    def fly(self):
        """Метод для взлета пассажирского самолета."""
        print(f"Пассажирский самолет '{self.model}' вместимостью {self.capacity} человек, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с пассажирами на борту.")


class CargoAircraft(Aircraft):
    """Класс для грузовых самолетов."""
    
    def fly(self):
        """Метод для взлета грузового самолета."""
        print(f"Грузовой самолет '{self.model}' грузоподъемностью {self.capacity} тонн, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с грузом на борту.")


class Airport:
    """Класс для управления аэропортом и самолетами."""
    
    def __init__(self):
        """Инициализирует пустой список для хранения самолетов."""
        self.aircrafts_list = []  

    def add_aircraft(self, aircraft: Aircraft):
        """Добавляет самолет в список аэропорта."""
        if isinstance(aircraft, Aircraft):
            self.aircrafts_list.append(aircraft)
        else:
            raise ValueError("Добавляемый объект должен быть экземпляром класса Aircraft или его подклассов.")

    def takeoff(self):
        """Метод для взлета всех самолетов в списке."""
        for aircraft in self.aircrafts_list:
            aircraft.fly()


# Создание экземпляра аэропорта
airport = Airport()

# Добавление различных самолетов в аэропорт
airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416)) 
airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70)) 
airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396)) 

# Взлет всех самолетов
airport.takeoff()
