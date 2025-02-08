class Aircraft:
    def __init__(self, model: str, manufacturer: str, capacity: int):
        self.model = model  
        self.manufacturer = manufacturer  
        self.capacity = capacity  


class PassengerAircraft(Aircraft):
    def fly(self):
        print(f"Пассажирский самолет '{self.model}' вместимостью {self.capacity} человек, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с пассажирами на борту.")


class CargoAircraft(Aircraft):
    def fly(self):
        print(f"Грузовой самолет '{self.model}' грузоподъемностью {self.capacity} тонн, "
              f"произведенный компанией {self.manufacturer}, поднимается в воздух с грузом на борту.")


class Airport:
    def __init__(self):
        self.aircrafts_list = []  


    def add_aircraft(self, aircraft: Aircraft):
        self.aircrafts_list.append(aircraft)


    def takeoff(self):
        for aircraft in self.aircrafts_list:
            aircraft.fly()


airport = Airport()
airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416)) 
airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70)) 
airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396)) 


airport.takeoff()
